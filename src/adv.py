from room import Room
from player import Player
from src.item import Item

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", 'outside'),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure'),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Put items in rooms

item1 = Item("Bone1", "Trash")
item2 = Item("Bone2", "Trash")
item3 = Item("Empty Chest", "Trash")
insect1 = Item("Poisonous spider", "Used to cook poisons for enemies")
animal1 = Item("Rat", "Used to cook Medium Panacea Potion")
# items for foyer
room['outside'].n_to.add_item(item1)
room['outside'].n_to.add_item(item2)
# items for overlook
room['foyer'].n_to.add_item(item1)
room['foyer'].n_to.add_item(item2)
# items for treasure
room['narrow'].n_to.add_item(item1)
room['narrow'].n_to.add_item(item2)
room['narrow'].n_to.add_item(item3)
# items for narrow
room['foyer'].e_to.add_item(item1)
room['foyer'].e_to.add_item(insect1)
room['foyer'].e_to.add_item(animal1)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input('Pleas enter your name\n')
player = Player(player_name, 'outside')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def divider():
    print("==================================================")


# repeat user input
def start_game():
    # * Prints the current room name
    divider()
    print(f"Current room: {room[str(player.current_room)].name}")
    # * Prints the current description
    print(f"Room description: {room[str(player.current_room)].description}")
    # * Prints items in the room
    print(f"Items in  {room[str(player.current_room)].name}: ")
    room[str(player.current_room)].get_items()
    # * Waits for user input and decides what to do.
    global user_input
    print("!!!Please choose to continue...!!!")
    user_input = input('[n] North [s] South [e] East [w] West [t] Take loot [i] Open inventory [d] Drop items [q] Finish The Game\n')


# welcome message
print(f'Welcome to Adventure Game {player.name}!')
start_game()


# check if link to room exists
def is_bound(m):
    if hasattr(m, '__self__'):
        divider()
        print("!!!DEADLOCK!!!")
    return hasattr(m, '__self__')


# move user to room
def move(obj, path):
    # get room instance
    current_room = getattr(obj, path)
    # change place of player
    player.__setattr__("current_room", current_room)


# put items in inventory
def open_inventory():
    while len(room[str(player.current_room)].items) > 0:
        for num, i in enumerate(room[str(player.current_room)].items):
            print(f"Do you want to take {i}?")
            u_i = input(f'[y] Yes [n] No [c] Close inventory\n')
            if u_i == 'y':
                player.add_item(i)
                room[str(player.current_room)].del_item(num)
            if u_i == 'c':
                return False

def manage_inventory():
    while len(player.inventory) > 0:
        for num, i in enumerate(player.inventory):
            print(f"Do you want to drop {i}?")
            u_i = input(f'[y] Yes [n] No [c] Close inventory\n')
            if u_i == 'y':
                del player.inventory[num]
                room[str(player.current_room)].add_item(i)
            if u_i == 'c':
                return False

# repl
while not user_input == 'q':
    if user_input == 'n' or user_input == 's' or user_input == 'e' or user_input == 'w':
        if user_input == 'n':
            if not is_bound(room[str(player.current_room)].n_to):
                move(room[str(player.current_room)], "n_to")
        if user_input == 's':
            if not is_bound(room[str(player.current_room)].s_to):
                move(room[str(player.current_room)], "s_to")
        if user_input == 'e':
            if not is_bound(room[str(player.current_room)].e_to):
                move(room[str(player.current_room)], "e_to")
        if user_input == 'w':
            if not is_bound(room[str(player.current_room)].w_to):
                move(room[str(player.current_room)], "w_to")
    elif user_input == 't':
        open_inventory()
    elif user_input == 'd':
        manage_inventory()
    elif user_input == 'i':
        divider()
        player.get_inventory()
    else:
        divider()
        print("Invalid selection pleas try again")
    start_game()
