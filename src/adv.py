from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# print(room['outside'].n_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

room_key_list = list(room.keys()) 
room_val_list = list(room.values()) 

player = Player("p1")

quit = False
while quit is False:
    print(f"\nYou are at the {room[player.current_room].name}")
    print(room[player.current_room].description)
    action = input("\nDo you go n, e, s, w, or q? ")

    if action == "n":
        if hasattr(room[player.current_room], 'n_to'):
            player.current_room = room_key_list[room_val_list.index(room[player.current_room].n_to)]
        else:
            print("\nYou can't go that north.")

    elif action == "e":
        if hasattr(room[player.current_room], 'e_to'):
            player.current_room = room_key_list[room_val_list.index(room[player.current_room].e_to)]
        else:
            print("\nYou can't go that east.")

    elif action == "s":
        if hasattr(room[player.current_room], 's_to'):
            player.current_room = room_key_list[room_val_list.index(room[player.current_room].s_to)]
        else:
            print("\nYou can't go that south.")

    elif action == "w":
        if hasattr(room[player.current_room], 'w_to'):
            player.current_room = room_key_list[room_val_list.index(room[player.current_room].w_to)]
        else:
            print("\nYou can't go that west.")

    elif action == "q":
        quit = True
    else:
        print("That is not a valid input")