#!/usr/bin/env python3

import random

def capitalized_list(names_list) -> list:
    i = 0
    for name in names_list:
        names_list[i] = names_list[i].capitalize()
        i += 1
    return (names_list)

def generate_name():
    names = ['alice', 'bob', 'charlie', 'dylan', 'emma', 'gregory', 'john', 'kevin', 'liam']
    BigLetter = True
    SmallLetter = False
    OnlyBigLetter = []
    i = 0
    for name in names:
        random_numb = random.randint(0, 1)
        if random_numb == BigLetter:
            names[i] = names[i].capitalize()
            OnlyBigLetter.append(names[i])
        else:
            names[i] = names[i].lower()
        i += 1
    return names, OnlyBigLetter

def score(player_list):
    players = {}
    for player in player_list:
        random_score = random.randint(100,500)
        players[player] = random_score
    return players
def show():
    names = generate_name()
    capitalized_names = capitalized_list(names[0])
    scores = score(capitalized_names)

    print(f"Initial list of players: {names[0]}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {names[1]}")
    print(f"\nScore dict: {scores}")

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    show()