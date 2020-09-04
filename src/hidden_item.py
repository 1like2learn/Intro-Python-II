from item import Item

class Hidden_item(Item):
  def __init__(self, name, description, key, hidden_room):
    super().__init__(name, description)
    self.key = key
    self.hiding_room = hidden_room
  def __str__(self):
    return super().__str__()