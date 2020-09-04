from room import Room
from player import Player
from item import Item
from hidden_item import Hidden_item
from dig import dig

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'meadow': Room("Secluded Meadow", 
    """Light filters into the tranquil meadow and illuminates
    a small mound of disturbed earth"""),

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

# Create the player
player = Player("p1")

#The room the player starts in

player.current_room = room['outside']

# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['meadow']
room['meadow'].w_to = room['outside']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Is the room illuminated

room['outside'].is_light = True
room['meadow'].is_light = True
room['foyer'].is_light = True
room['overlook'].is_light = True
room['narrow'].is_light = False
room['treasure'].is_light = False

#Add items to rooms

shovel = Item("shovel", "a worn but sturdy shovel.")
lamp = Hidden_item("lamp", "a dusty but functional gas oil lamp.", shovel, room['meadow'])
room['overlook'].__add_item__(shovel)
lamp.item_found = False

# Add description if a shovel has been used
room['meadow'].dug_description = """Light filters into the tranquil meadow and illuminates
a small hole you dug"""

room['meadow'].dug2_description = """The once tranquil meadow looks like a troop
of coked out miners tried to dig a latrine."""

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

item_found = False
quit = False
while quit is False:
    current_room = player.current_room
    print(f"\nYou are at the {current_room.name}")

    if current_room.is_light or lamp in player.inventory:
        print(current_room.description)
        if len(current_room.items) > 0:
            for item in current_room.items:
                print(f"\nThere is a {item.name} here.\nIt is {item.description}")
    else:
        print("It's pitch black!")
        
    action = input("\nDo you go n, e, s, w, or q? ").split(' ')

    if action[0] == "n" and len(action) == 1:
        player.call_move('n_to')

    elif action[0] == "e" and len(action) == 1:
        player.call_move('e_to')

    elif action[0] == "s" and len(action) == 1:
        player.call_move('s_to')

    elif action[0] == "w" and len(action) == 1:
        player.call_move('w_to')
    
    elif action[0] == "get" and len(action) == 2:
        player.call_pickup_item(action[1])
    
    elif action[0] == "drop" and len(action) == 2:
        player.call_drop_item(action[1])

    elif action[0] == "dig" and len(action) == 1:
        item_found = dig(lamp, player, item_found)
#         if player.current_room == room['meadow'] and not lantern_found and shovel in player.inventory:
#             print("\nYou found a gas lantern to light your way")
#             player.call_pickup_item(lamp)
#             lantern_found = True
#             room['meadow'].description = """Light filters into the tranquil meadow and illuminates
# a small hole you dug"""

#         elif player.current_room == room['meadow'] and not lantern_found and not shovel in player.inventory:
#             print("\nYou spend a few minutes dirtying your fingers and give up when you grow tired.")

#         elif player.current_room == room['meadow'] and lantern_found and shovel in player.inventory:
#             print("\nYou dig a few more holes but find nothing")
#             room['meadow'].description = """The once tranquil meadow looks like a troop
# of coked out miners tried to dig a latrine."""

#         elif player.current_room == room['meadow'] :
#             print("\nYou can't dig here.")

    elif action[0] == "i" and len(action) == 1:
        player.call_check_inventory()

    elif action[0] == "q" and len(action) == 1:
        quit = True

    else:
        print("\nThat is not a valid input")