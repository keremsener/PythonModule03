import sys


def score_analytics():
    array = []
    i = 1
    total_arg = len(sys.argv) - 1
    while i <= total_arg:
        try:
            array.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1

    if len(array) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py\
 <score1> <score2> ...")
    else:
        print("Scores processed:", array)
        print("Total players:", len(array))
        print("Total score:", sum(array))
        print("Average score:", sum(array) / len(array))
        print("High score:", max(array))
        print("Low score:", min(array))
        print("Score range:",  max(array) - min(array))


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
