#!/usr/bin/env python3

import random

def capitalized_list(names_list) -> list:
    return [name.capitalize() for name in names_list]

def generate_name() -> tuple[list[str], list[str]]:
    names = ['alice', 'bob', 'charlie', 'dylan', 'emma', 'gregory', 'john', 'kevin', 'liam']
    BigLetter = True

    new_names = [name.capitalize() if random.randint(0, 1) == BigLetter else name.lower() for name in names]
    OnlyBigLetter = [name for name in new_names if name.istitle()]
    return new_names, OnlyBigLetter

def score(player_list):
    return {player: random.randint(100,500) for player in player_list}

def average(scores:dict) -> float:
    result = sum(scores.values()) / len(scores)
    return (round(result, 2))


def high_score(player_scores: dict[str, int], avg: float) -> dict[str, int]:
    return {player: score for player, score in player_scores.items() if score > avg}


def show():
    names = generate_name()
    capitalized_names = capitalized_list(names[0])
    scores = score(capitalized_names)
    average_score = average(scores)
    high_score_list = high_score(scores, average_score)

    print(f"Initial list of players: {names[0]}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {names[1]}")
    print(f"\nScore dict: {scores}")
    print(f"Score average is {average_score}")
    print(f"High scores: {high_score_list}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    show()