# 4. Inventory Tracker 
# Imagine a small store inventory like {"apple": 10, "banana": 5, "milk": 2}. Program should allow 
# adding new items, selling items (subtract quantity), and print items that are low in stock (<3).

inventory = {
    "apple": 10,
    "banana": 5,
    "milk": 2
}

def add_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"{quantity} {name} added.")

def sell_item(name, quantity):
    if name in inventory:
        if inventory[name] >= quantity:
            inventory[name] -= quantity
            print(f"{quantity} {name} sold.")
        else:
            print("Not enough stock available!")
    else:
        print("Item not found in inventory.")


def low_stock_items():
    print("\nItems low in stock (less than 3):")
    for item, qty in inventory.items():
        if qty < 3:
            print(f"{item}: {qty}")

add_item("apple", 5)
sell_item("banana", 2)
sell_item("milk", 1)

print("\nUpdated Inventory:")
for item, qty in inventory.items():
    print(f"{item}: {qty}")

low_stock_items()
