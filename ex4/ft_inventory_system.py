#!/usr/bin/env python3
import sys


class InventorError(Exception):
    def __init__(self, name):
        super().__init__(name)


def parse_item(arg):
    parts = arg.split(":")
    if len(parts) != 2:
        raise InventorError(f"Error invalid parameter '{arg}'")
    return parts[0], parts[1]


def most_abundant(items):
    try:
        most_amount = list(items.values())[0]
        most_name = list(items.keys())[0]
    except IndexError:
        print("Enter an Arg!")
        exit()
    for name, amount in items.items():
        if (amount > most_amount):
            most_amount = amount
            most_name = name
    print(f"Item most abundant: {most_name} with quantity {most_amount}")


def least_abundant(items):
    least_amount = list(items.values())[0]
    least_name = list(items.keys())[0]
    for name, amount in items.items():
        if (amount < least_amount):
            least_amount = amount
            least_name = name
    print(f"Item least abundant: {least_name} with quantity {least_amount}")


def show(items):
    total_amount = sum(items.values())
    print(f"Got inventory: {items}")
    print(f"Item list: {list(items.keys())}")
    print(f"Total quantity of the {len(items)} items: {total_amount}")

    for name, amount in items.items():
        percentage = (amount / total_amount) * 100
        rounded_percentage = round(percentage, 1)
        print(f"Item {name} represents {rounded_percentage}%")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    i = 1
    items = {}
    while i < len(sys.argv):
        try:
            name, amount = parse_item(sys.argv[i])
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
    show(items)
    most_abundant(items)
    least_abundant(items)
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")
