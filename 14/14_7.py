import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    half = n // 2

    first_queue = deque()
    for i in range(1, half + 1):
        first_queue.append(int(input_data[i]))

    second_queue = deque()
    for i in range(half + 1, n + 1):
        second_queue.append(int(input_data[i]))

    moves = 0
    max_moves = 200000

    while first_queue and second_queue and moves < max_moves:
        moves += 1
        c1 = first_queue.popleft()
        c2 = second_queue.popleft()

        first_wins = False
        if c1 == 0 and c2 == n - 1:
            first_wins = True
        elif c2 == 0 and c1 == n - 1:
            first_wins = False
        elif c1 > c2:
            first_wins = True
        else:
            first_wins = False

        if first_wins:
            first_queue.append(c1)
            first_queue.append(c2)
        else:
            second_queue.append(c1)
            second_queue.append(c2)

    if not first_queue:
        print(f"second {moves}")
    elif not second_queue:
        print(f"first {moves}")
    else:
        print("draw")


if __name__ == "__main__":
    solve()