#!/usr/bin/env python3
import math


def get_player_pos() -> tuple:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinate = text.split(",")

        if len(coordinate) != 3:
            print("Invalid syntax")
            continue

        error_found = False
        for item in coordinate:
            try:
                float(item)
            except ValueError as e:
                print(f"Error on parameter '{item}': {e}")
                error_found = True
                break

        if error_found:
            continue

        return (float(coordinate[0]), float(coordinate[1]),
                float(coordinate[2]))


def coordinate_sytem():
    print("Get a first set of coordinates")
    array = []
    player_pos = get_player_pos()
    array.append(player_pos)
    print(f"Got a first tuple: {player_pos}")
    text = "It includes:"
    print(f"{text} X={player_pos[0]}, Y={player_pos[1]}, Z={player_pos[2]}")
    distance = math.sqrt((player_pos[0] - 0)**2 + (player_pos[1] - 0)**2 +
                         (player_pos[2] - 0)**2)

    print("Distance to center:", round(distance, 4))
    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()
    second_distance = math.sqrt((player_pos[0] - second_pos[0])**2 +
                                (player_pos[1] - second_pos[1])**2 +
                                (player_pos[2] - second_pos[2])**2)
    text = "Distance between the 2 sets of coordinates:"
    print(f"{text} {round(second_distance, 4)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    coordinate_sytem()
