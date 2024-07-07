
def display_inventory(inventory: dict) -> None:
    total = 0
    print("Inventory:")
    for item, count in inventory.items():
        total += count
        print(count, item)
    print("Total number of items:", total)


def add_to_inventory(inventory: dict, added_items: list[str]) -> None:
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
    


my_inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(my_inv)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
