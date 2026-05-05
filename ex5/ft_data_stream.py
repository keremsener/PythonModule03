#!/usr/bin/env python3
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "use", "release"]
    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(array: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while array:
        current_action = random.choice(array)
        array.remove(current_action)
        yield current_action


def manage_events() -> None:
    print("=== Game Data Stream Processor ===")
    player: list[tuple[str, str]] = []
    counter = 0
    event_stream = gen_event()
    for i in range(1000):
        current_event = next(event_stream)
        if counter != 10:
            new_list_10_event = next(event_stream)
            player.append(new_list_10_event)
            counter += 1
        print(
            f"Event {i}: Player {current_event[0]} did action {current_event[1]}")
    print("Built list of 10 events:", player)

    for consumed in consume_event(player):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {player}")


if __name__ == "__main__":
    manage_events()
