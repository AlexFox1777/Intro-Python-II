# Write a class to hold player information, e.g. what room they are in
# currently.
from src.item import Item


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def get_inventory(self):
        print("!!!Inventory!!!")
        if len(self.inventory) > 0:
            print(f"Amount of items: {len(self.inventory)}")
            for num, name in enumerate(self.inventory, start=1):
                print(f'Item {num}: {name}')
        else:
            print("Inventory is empty!")

    def add_item(self, item):
        if type(item) is Item:
            self.inventory.append(item)
        else:
            print(f"{item} is not an Item")

    def __str__(self):
        return f"{self.name} is in the {self.current_room} room"
