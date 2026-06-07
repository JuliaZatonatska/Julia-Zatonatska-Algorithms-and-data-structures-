import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    unique_numbers = set(input_data[1:n + 1])

    print(len(unique_numbers))


if __name__ == '__main__':
    solve()