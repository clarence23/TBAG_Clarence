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

     
