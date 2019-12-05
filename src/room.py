# Implement a class to hold room information. This should have name and
# description attributes.
from src.item import Item


class Room:
    def __init__(self, name, description, key):
        self.items = []
        self.name = name
        self.description = description
        self.key = key

    def n_to(self):
        pass

    def s_to(self):
        pass

    def e_to(self):
        pass

    def w_to(self):
        pass

    def __str__(self):
        return f'{self.key}'

    def add_item(self, item):
        if type(item) is Item:
            self.items.append(item)
        else:
            print(f'{item} is not an Item')

    def del_item(self, id):
        if len(self.items) > 0:
            del self.items[id]

    def get_items(self):
        if len(self.items) > 0:
            for i in self.items:
                print(i)
        else:
            print("No items in the room")
