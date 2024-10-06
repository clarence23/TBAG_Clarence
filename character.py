class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation): 
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says {self.conversation}]")
        else:
            print(f"{self.name} doesn't want to talk to you!")

    def fight(self):
        print(f"{self.name} doesn't want to fight with you!")
        return True                      


class Enemy(Character):
    def __init__(self, char_name, char_description, loot=None):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.is_asleep = False
        self.loot = loot
        self.loot_stolen = False
        self.sleep_attempted = False  # Track if sleep has been attempted

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness   

    def get_weakness(self):
        return self.weakness   

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}!!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def bribe(self, amount):
        if amount >= 10:  # Arbitrary bribe amount
            print(f"{self.name} accepts your bribe of £{amount} and lets you pass!")
            return True
        else:
            print(f"{self.name} refuses to be bribed with ${amount}.")
            return False

    def steal(self):
        if self.loot_stolen:
            print(f"There's nothing left to steal from {self.name}.")
            return False
        elif not self.is_asleep:
            print(f"{self.name} catches you trying to steal!")
            return False
        else:
            print(f"You successfully steal {self.loot} from {self.name}!")
            self.loot_stolen = True
            return True

    def put_to_sleep(self, sleep_item):
    # If already asleep and player attempts again, enemy catches and kills
        if self.is_asleep and self.sleep_attempted:
            print(f"{self.name} wakes up, catches you trying to use {sleep_item} again, and kills you!")
            print("Game Over.")
            exit()  # End game if caught trying to put to sleep multiple times
    
    # If already asleep but no sleep was attempted yet
    #    if self.is_asleep:
    #        print(f"{self.name} is already asleep!")
    #        return True
    
    # First attempt: Use valid sleep item
        if sleep_item in ["sleeping powder"]:
            print(f"You throw {sleep_item}, and {self.name} falls asleep! But think fast it's only temporary")
            self.is_asleep = True
            self.sleep_attempted = True  # Mark that sleep was attempted
            return True
    
    # Wrong item used, enemy catches player and kills them
        else:
            print(f"{self.name} catches you trying to use {sleep_item} and kills you!")
            print("Game Over.")
            exit()  # End game if wrong item is used

# Friend class extending Character
class Friend(Character):
    def __init__(self, char_name, char_description, favorite_gift):
        super().__init__(char_name, char_description)
        self.favorite_gift = favorite_gift

    def hug(self):
        print(f"{self.name} hugs you warmly!")

    def give_gift(self, gift):
        if gift == self.favorite_gift:
            print(f"{self.name} happily accepts the {gift}!")
        else:
            print(f"{self.name} politely declines the {gift}.")
