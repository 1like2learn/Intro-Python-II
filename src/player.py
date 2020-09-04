# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name):
    self.name = name
    self.inventory = []
    self.current_room = {}
    
  def __pickup_item__(self, new_item):
    for item in self.current_room.items:
      if new_item == item.name:
        self.inventory.append(item)
        self.current_room.call_remove_item(item)
        print(f"\nYou picked up the {item.name}")
      else:
        print("\nYou can't pickup an item that isn't in this room.")

  def call_pickup_item(self, item):
    self.__pickup_item__(item)

  def __drop_item__(self, item_drop):
    for item in self.inventory:
      if item_drop == item.name:
        self.inventory.remove(item)
        self.current_room.call_add_item(item)
        print(f"\nYou dropped the {item.name}")
      else:
        print("\nYou can't an item you don't have.")

  def call_drop_item(self, item):
    self.__drop_item__(item)

  def __move__(self, direction):
    if hasattr(self.current_room, direction):
      self.current_room = getattr(self.current_room, direction)

    else:
      print("\nYou can't go that way.")

  def call_move(self, direction):
    self.__move__(direction)

  def __check_inventory__(self):
    if len(self.inventory) > 0:
      for item in self.inventory:
        print(item)
    else:
      print("\nYour inventory is empty.")

  def call_check_inventory(self):
    self.__check_inventory__()
  
  def __get_hidden_item(self, item):
    self.inventory.append(item)

  def call_get_hidden_item(self, item):
    self.__get_hidden_item(item)