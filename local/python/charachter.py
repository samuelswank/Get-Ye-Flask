from room import Room

class Player:
    def __init__(self, name, sex, current_room, inventory, score):
        self.name = name
        self.sex = sex
        self.current_room = current_room
        self.inventory = []
        self.score = 0

    def get_item(self, item):
        self.current_room.items.remove(item)
        self.inventory.append(item)

        