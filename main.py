from room import Room
from character import Enemy
from character import Friend

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
living_room = Room("Living Room")
locked_room = Room("Locked Room")


dave = Enemy("Dave", "A smelly zombie", loot="golden ring")
dave.set_conversation("Hi, I'm Dave and totally won't eat your brains")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

bob = Enemy("Bob", "A sneaky thief.", "pocket watch")
bob.set_conversation("Hey! What are you doing here?")
bob.set_weakness("light")
ballroom.set_character(bob)

# Create a Friend character
linda = Friend("Linda", "A friendly villager who loves flowers.", favorite_gift="flowers")
living_room.set_character(linda)

kitchen.set_description("A dark and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor.")
dining_hall.set_description("A large room with ornate golden decorations.")
locked_room.set_description("A mysterious room, previously locked. What secrets does it hold?")

# Link rooms
kitchen.link_room(dining_hall, "south")
kitchen.link_room(living_room, "east")
living_room.link_room(dining_hall, "north")
dining_hall.link_room(kitchen, "east")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(locked_room, "east")
locked_room.link_room(ballroom, "south")
locked_room.link_room(kitchen, "north")

# Main game loop
player_inventory = ["sleeping powder"]  

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    # Handle character interactions
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

 # If the inhabitant is a Friend
        if isinstance(inhabitant, Friend):
            print("\nYou meet a friend! What do you want to do?")
            print("1. Hug")
            print("2. Give a gift")

            choice = input("Choose an action: ")

            if choice == "1":  # Hug
                inhabitant.hug()
            
            elif choice == "2":  # Give a gift
                gift = input("What gift would you like to give? ")
                inhabitant.give_gift(gift)

        # If the inhabitant is Dave (a zombie)
        elif isinstance(inhabitant, Enemy) and inhabitant.name == "Dave":
            # Automatically make Dave speak
            inhabitant.talk()

            while True:
                print("\nYou encounter Dave! What do you want to do?")
                print("1. Fight")
                print("2. Steal")
                print("3. Put to Sleep (throw 'sleeping powder')")

                choice = input("Choose an action: ")

                if choice == "1":  # Fight
                    fight_with = input("What item will you fight with?: ")
                    if inhabitant.fight(fight_with):
                        print("You won the fight!")
                        break
                    else:
                        print("You lost the fight! Game Over.")
                        exit()

                elif choice == "2":  # Steal
                    if inhabitant.steal():
                        break
                    else:
                        print(f"{inhabitant.name} catches you trying to steal and kills you!")
                        print("Game Over.")
                        exit()
                        
                elif choice == "3":  # Put to sleep
                    sleep_item = input("What item will you use to put Dave to sleep?: ")
                    if sleep_item in player_inventory:
                        inhabitant.put_to_sleep(sleep_item)
                        break
                    else:
                        print(f"You don't have {sleep_item} in your inventory!")

                else:
                    print("Invalid choice.")
        
        # If the inhabitant is Bob (a thief)
        elif isinstance(inhabitant, Enemy) and inhabitant.name == "Bob":
            # Automatically make Bob speak
            inhabitant.talk()

            while True:
                print("\nYou encounter Bob! What do you want to do?")
                print("1. Fight")
                print("2. Bribe (with money)")
                print("3. Steal")
                print("4. Put to Sleep (throw 'sleeping powder')")

                choice = input("Choose an action: ")

                if choice == "1":  # Fight
                    fight_with = input("What item will you fight with?: ")
                    if inhabitant.fight(fight_with):
                        print("You won the fight!")
                        break
                    else:
                        print("You lost the fight! Game Over.")
                        exit()

                elif choice == "2":  # Bribe (with money)
                    try:
                        amount = int(input("Enter the bribe amount: "))
                        if inhabitant.bribe(amount):
                            print("You successfully bribed Bob.")
                            break  # Exit the loop after a successful bribe
                        else:
                            print(f"{inhabitant.name} gets angry because the bribe is too low and kills you!")
                            print("Game Over.")
                            exit()
                    except ValueError:
                        print("Invalid amount.")

                elif choice == "3":  # Steal
                    if inhabitant.steal():
                        break
                    else:
                        print(f"{inhabitant.name} catches you trying to steal and kills you!")
                        print("Game Over.")
                        exit()

                elif choice == "4":  # Put to sleep
                    sleep_item = input("What item will you use to put Bob to sleep?: ")
                    if sleep_item in player_inventory:
                        inhabitant.put_to_sleep(sleep_item)
                        break
                    else:
                        print(f"You don't have {sleep_item} in your inventory!")

                else:
                    print("Invalid choice.")
    else:
        print("There's no one here.")
    
     # Handle Locked Room interaction
    if current_room == locked_room:
        while True:
            print("\nYou are in front of the locked door. Do you want to:")
            print("1. Unlock the door")
            print("2. Leave the room")

            choice = input("Choose an action: ")

            if choice == "1":  # Unlock the door
                key_name = input("Enter the name of the key: ")
                if key_name.lower() == "golden key":  # Check if the player has the correct key
                    print("You unlocked the door successfully! Looks like you're in the basement, The room holds mysterious treasures.")
                    break  # Successfully unlocked the room, exit the loop
                else:
                    print("That's the wrong key. Try again!")

            elif choice == "2":  # Leave the room
                print("You decide to leave the room.")
                break  # Allow the player to leave without unlocking the door

            else:
                print("Invalid choice.")

    # Move to a new room
    direction = input("Which direction do you want to go?: ")
    new_room = current_room.move(direction)
    if new_room != current_room:  # Only update the current room if the move was successful
        current_room = new_room
