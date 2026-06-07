import sys
from collections import deque


def solve():
    queue = deque()

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue

        command = parts[0]

        if command == "push":
            n = parts[1]
            queue.append(n)
            print("ok")
        elif command == "pop":
            if queue:
                print(queue.popleft())
            else:
                print("error")
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print("error")
        elif command == "size":
            print(len(queue))
        elif command == "clear":
            queue.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    solve()