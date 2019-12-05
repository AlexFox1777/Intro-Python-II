from room import Room
from player import Player

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
    # * Waits for user input and decides what to do.
    global user_input
    print("!!!Please choose to continue...!!!")
    user_input = input('[n] North [s] South [e] East [w] West\n')


# welcome message
print(f'Welcome to Adventure Game {player.name}!')
start_game()


# check if the path exists
def is_bound(m):
    if hasattr(m, '__self__'):
        divider()
        print("!!!DEADLOCK!!!")
    return hasattr(m, '__self__')


# repl
while not user_input == 'q':
    if user_input == 'n' or user_input == 's' or user_input == 'e' or user_input == 'w':
        if user_input == 'n':
            if not is_bound(room[str(player.current_room)].n_to):
                current_room = room[str(player.current_room)].n_to
                player.set_room(current_room)
        if user_input == 's':
            if not is_bound(room[str(player.current_room)].s_to):
                current_room = room[str(player.current_room)].s_to
                player.set_room(current_room)
        if user_input == 'e':
            if not is_bound(room[str(player.current_room)].e_to):
                current_room = room[str(player.current_room)].e_to
                player.set_room(current_room)
        if user_input == 'w':
            if not is_bound(room[str(player.current_room)].w_to):
                current_room = room[str(player.current_room)].w_to
                player.set_room(current_room)
    else:
        divider()
        print("Invalid selection pleas try again")
    start_game()
