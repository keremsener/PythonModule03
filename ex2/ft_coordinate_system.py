def get_player_pos(numb: list) -> tuple:

    return (float(numb[0]), float(numb[1]), float(numb[2]))


def convert_float():
    while True:
        try:
            split = input("Enter new coordinates as floats in format 'x,y,z':\
 ").split(",")
            split = get_player_pos(split)
            break
        except ValueError:
            print("Invalid syntax")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    convert_float()
