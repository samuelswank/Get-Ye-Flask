class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, dennis_to=None):
        self.name = name
        self.description = description

        self.items = []