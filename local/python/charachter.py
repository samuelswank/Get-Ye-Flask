from room import Room

class Player:
    def __init__(self, current_room, inventory=[], score=0):
        self.current_room = current_room
        self.inventory = inventory
        self.score = score

    def get_item(self, item):
        self.current_room.items.remove(item)
        self.inventory.append(item)

    