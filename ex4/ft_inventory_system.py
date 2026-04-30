#!/usr/bin/env python3
import sys

if __name__ ==  "__main__":
    print("=== Inventory System Analysis ===")
    i = 1
    items = {}
    while i < len(sys.argv):
        items = sys.argv[i].split(":")
        i += 1
    print(items)