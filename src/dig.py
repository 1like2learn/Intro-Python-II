def dig(hidden_item, player, item_found):
  key, hiding_room = hidden_item.key, hidden_item.hiding_room
  print("item found", item_found)
  if player.current_room == hiding_room and not item_found and key in player.inventory:
    print("\nYou found a gas lantern to light your way")
    player.call_get_hidden_item(hidden_item)
    hiding_room.description = hiding_room.dug_description
    return True

  elif player.current_room == hiding_room and not key in player.inventory:
    print("\nYou spend a few minutes dirtying your fingers and give up when you grow tired.")
    return False

  elif player.current_room == hiding_room and item_found and key in player.inventory:
    print("\nYou dig a few more holes but find nothing")
    hiding_room.description = hiding_room.dug2_description
    return True

  elif player.current_room != hiding_room :
    print("\nYou can't dig here.")
    return False