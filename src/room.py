# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, key):
        self.name = name
        self.description = description
        self.key = key
        self.items = []

    def n_to(self, room):
        return room.name

    def s_to(self, room):
        return room.name

    def e_to(self, room):
        return room.name

    def w_to(self, room):
        return room.name

    def __str__(self):
        return f'{self.key}'

    def items(self, item):
        self.items.append(item)
        return f"Item {item} was successfully added to list"






