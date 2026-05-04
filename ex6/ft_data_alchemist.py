#!/usr/bin/env python3

import random

def capitalized_list(names_list) -> list:
    i = 0
    for name in names_list:
        names_list[i] = names_list[i].capitalize()
        i += 1
    return (names_list)


def generate_name() -> tuple[list[str], list[str]]:
    names = ['alice', 'bob', 'charlie', 'dylan', 'emma', 'gregory', 'john', 'kevin', 'liam']
    BigLetter = True
    SmallLetter = False

    new_names = [name.capitalize() if random.randint(0, 1) == BigLetter else name.lower() for name in names]
    OnlyBigLetter = [name for name in new_names if name.istitle()]
    return new_names, OnlyBigLetter

def score(player_list):
    players = {}
    for player in player_list:
        random_score = random.randint(100,500)
        players[player] = random_score
    return players

def average(scores:dict) -> float:
    result = sum(scores.values()) / len(scores)
    return (round(result, 2))

def high_score(player_scores: dict) -> dict:
    players = {}
    temp_scores = player_scores.copy()
    
    for _ in range(5):
        if not temp_scores:
            break

        best_player = max(temp_scores, key=temp_scores.get)
        players[best_player] = temp_scores[best_player]
        temp_scores.pop(best_player)
        
    return players

def show():
    names = generate_name()
    capitalized_names = capitalized_list(names[0])
    scores = score(capitalized_names)
    average_score = average(scores)
    high_score_list = high_score(scores)

    print(f"Initial list of players: {names[0]}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {names[1]}")
    print(f"\nScore dict: {scores}")
    print(f"Score average is {average_score}")
    print(f"High scores: {high_score_list}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    show()