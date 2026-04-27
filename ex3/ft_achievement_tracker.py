#!/usr/bin/env python3
import random

achievements_pool = [
    "Crafting Genius", "Strategist", "World Savior",
    "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Unstoppable", "First Steps",
    "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
]


def gen_player_achievements() -> list:
    random_numb = random.randint(4, 8)
    player_achievement = set(random.sample(achievements_pool, random_numb))
    return (player_achievement)


class control:
    def __init__(self, array):
        self.array = array

    def common_control(self):
        common_array = set.intersection(self.array)
        if not common_array:
            print("Common achievements: ❌")
        else:
            print(f"Common achievements: {self.array}")


if __name__ == "__main__":
    i = 0
    player_name = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements = ["Alice", "Bob", "Charlie", "Dylan"]
    for i in 0, 1, 2, 3:
        player_achievements[i] = gen_player_achievements()
        print(f"Player {player_name[i]}: {player_achievements[i]}")
        i += 1
    print(player_achievements[0])
    print("\nAll distinct achievements:", achievements_pool)
    # control.common_control()

