class Room:
    def __init__(self, name, description, north_to=None, south_to=None, dennis_to=None, not_dennis_to=None):
        self.name = name
        self.description = description

        self.items = []