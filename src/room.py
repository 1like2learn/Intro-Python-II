# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []
    
  def __add_item__(self, item):
    self.items.append(item)

  def call_add_item(self, item):
    self.__add_item__(item)

  def __remove_item__(self, item):
    self.items.remove(item)

  def call_remove_item(self, item):
    self.__remove_item__(item)
  # def __str__(self):
  #   self.keys()