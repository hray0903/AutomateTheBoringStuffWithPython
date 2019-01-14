stuff = {"rope": 1, "torch": 6,
              "gold coin": 42, "dirk": 1, "arrow": 12}

def display_inventory(inventory):
    print("belongings list:")
    item_total = 0
    for item, num in inventory.items():
        print(str(num) + " " + item)
        item_total += num
    print("total amount:" + " " + str(item_total))

display_inventory(stuff)

dragon_loot = ["gold coin", "dirk", "gold coin", "gold coin", "ruby"]

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
