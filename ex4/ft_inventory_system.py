#!/usr/bin/env python3
import sys

class InventorError(Exception):
    def __init__(self, name):
        super().__init__(name)

def items__(arg):
    parts = arg.split(":")
    if len(parts) != 2:
        raise InventorError(f"Error invalid parameter '{arg}'")    
    return parts[0], parts[1]

def show(items, total_amount):
    print(f"Got inventory: {items}")
    print(f"Item list: {list(items.keys())}")
    print(f"Total quantity of the {len(items)} items: {total_amount}")

    for name, amount in items.items():
        percentage = (amount / total_amount) * 100
        rounded_percentage = round(percentage, 1)
        print(f"Item {name} represents {rounded_percentage}%")

if __name__ ==  "__main__":
    print("=== Inventory System Analysis ===")
    i = 1
    items = {}
    while i < len(sys.argv):
        try:
            name, amount = items__(sys.argv[i])
            if name in items:
                print(f"Redundant item '{name}' - discarding")
            else:
                try:
                    items[name] = int(amount)
                except ValueError as e:
                    print(f"Quantity error for '{name}': {e}")
        except InventorError as e:
            print(e)
        i += 1
    total_amount = sum(items.values())
    show(items, total_amount)