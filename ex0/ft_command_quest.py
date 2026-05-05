import sys


def command_quest():
    total_arg = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if total_arg <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_arg - 1}")
        i = 1
        while i < total_arg:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {total_arg}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
