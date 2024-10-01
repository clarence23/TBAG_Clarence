from room import Room
from character import Enemy

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hi im Dave and totally wont eat your brains")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

kitchen.set_description("A dark and dirty room buzzing with files")
#print(kitchen.get_description())
ballroom.set_description("A vast room with a w=shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
       inhabitant.describe()
    command = input("> ")
    current_room = current_room.move(command)

     
#def convert():
#    weight = int(input("What do you weight?: "))
#    unit = str(input("Is that [K]gs or [L]bs?: "))
#    if unit.lower() == 'k':
#        lbs = weight * 2.2
#        print("Your weight in lbs is:", lbs)
#    elif unit.lower() == 'l':
#        kg = weight * 0.45
#        print("Your weight in kgs is: ", kg)
#    else:
#        print("Sorry, try again")

#convert() 

#def bootcamp_welcome(bootcamp):
#    print(f"Welcome to the {bootcamp} bootcamp")

#bootcamp_welcome('Software engineering') 
#bootcamp_welcome('Data analytics') 
#bootcamp_welcome('Cloud engineering')    

#def cash_machine(acc_num, sort_code, amount):
#    print(f"Withdrawing £{amount}\nAccount Number: {acc_num}\nSort Code: {sort_code}")

#cash_machine(1234556, 304055, 250)

#def my_func():
#    name = input('Enter your name here: ')
#    age = int(input('Enter your age here: '))
#    print(f"Happy birthday {name} i hear your are {age} today!")

#my_func()

#import random 

#for i in range(6):
#    number = random.randint(1, 30)
#    if number % 7 == 0:
#        print(f"{number} is divisible by 7")
#    else:
#        print(f"{number} is not divisible by 7")    

#def cash_machine():

#    pin = 1234
#    balance = 1000

#    attempts = 3

#    while attempts > 0:
#        user_pin = int(input("Enter your 4-digit PIN: "))
#        if user_pin == pin:
#            print("PIN accepted.")
#            break
#        else:
#            attempts -= 1
#            print(f"Incorrect PIN. You have {attempts} attempts left.")
#    else:
#        print("Too many incorrect attempts. Access denied.")
#        return
#
#    while True:
#        print("\n--- ATM MENU ---")
#        print("1. Check Balance")
#        print("2. Withdraw Cash")
#        print("3. Exit")
#        choice = int(input("Choose an option: "))
#
#        if choice == 1:
#            print(f"Your current balance is: £{balance}")
#
#        elif choice == 2:
#            withdraw_amount = int(input("Enter amount to withdraw: £"))
#
#            if withdraw_amount > balance:
#                print("Insufficient balance!")
#            elif withdraw_amount <= 0:
#                print("Invalid amount!")
#            else:
#                balance -= withdraw_amount
#                print(f"Please collect your £{withdraw_amount}.")
#                print(f"Your remaining balance is: £{balance}")

#        elif choice == 3:
#            print("Thank you for using the ATM. Goodbye!")
#            break

#        else:
#            print("Invalid choice, please try again.")


# Run the cash machine app by invoking the function
#cash_machine()

#import random 
#def roll_dice():
#  dice_roll = random.randint(1, 6)
#  if dice_roll == 6:
#    print("Congrats, move 6 spaces!")
#  else:
#    print(dice_roll)
#    print("Try again")
#roll_dice()  
