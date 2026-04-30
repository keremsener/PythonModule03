#!/usr/bin/env python3
import sys

if __name__ ==  "__main__":
    print("=== Inventory System Analysis ===")
    i = 1
    items = {}
    while i < len(sys.argv):
        if len(parts) < 2:
            print (f"Error invalid parameter '{parts[0]}'")
        else:
            parts = sys.argv[i].split(":")
        print(parts)
        i += 1