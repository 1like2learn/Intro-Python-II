# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name):
    self.name = name
    self.current_room = "outside"
    self.inventory = []
    
  def __pickup_item__(self, item):
    self.inventory.append(item)

  def call_add_item(self, item):
    self.__pickup_item__(item)

  def __drop_item__(self, item):
    self.inventory.remove(item)

  def call_remove_item(self, item):
    self.__drop_item__(item)