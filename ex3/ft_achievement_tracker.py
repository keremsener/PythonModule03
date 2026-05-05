#!/usr/bin/env python3
import random

achievements_pool = [
    "Crafting Genius", "Strategist", "World Savior",
    "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Unstoppable", "First Steps",
    "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    random_numb = random.randint(4, 8)
    player_achievement = set(random.sample(achievements_pool, random_numb))
    return (player_achievement)


class Control:
    def __init__(self, array: list[set[str]], name: list[str]) -> None:
        self.array = array
        self.name = name

    def common_control(self) -> None:
        common_array = set.intersection(*self.array)
        if not common_array:
            print("\nCommon achievements: ❌")
        else:
            print(f"\nCommon achievements: {common_array}")

    def all_distinct_control(self) -> set[str]:
        return set.union(*self.array)

    def exclusive_control(self) -> None:
        for i in range(len(self.array)):
            current_player_set = self.array[i]
            current_player_name = self.name[i]

            exclusive_set = current_player_set.copy()

            for j in range(len(self.array)):
                if i != j:
                    exclusive_set = exclusive_set.difference(self.array[j])
            print(f"Only {current_player_name} has: {exclusive_set}")

    def missing_control(self) -> None:
        total = self.all_distinct_control()
        for i in range(len(self.array)):
            current_player_set = self.array[i]
            current_player_name = self.name[i]
            missing_set = total.difference(current_player_set)
            print(f"{current_player_name} is missing: {missing_set}")


def achievement_tracker() -> None:
    i = 0
    player_name = ["Alice", "Bob", "Charlie", "Dylan"]
    player_achievements: list[set[str]] = [set() for _ in range(4)]
    for i in range(4):
        player_achievements[i] = gen_player_achievements()
        print(f"Player {player_name[i]}: {player_achievements[i]}")

    my_control = Control(player_achievements, player_name)

    print("\nAll distinct achievements:", my_control.all_distinct_control())
    my_control.common_control()
    print()
    my_control.exclusive_control()
    print()
    my_control.missing_control()


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achievement_tracker()
