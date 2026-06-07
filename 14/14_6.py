import sys
from collections import deque


def solve():
    deq = deque()

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue

        command = parts[0]

        if command == "push_front":
            n = parts[1]
            deq.appendleft(n)
            print("ok")
        elif command == "push_back":
            n = parts[1]
            deq.append(n)
            print("ok")
        elif command == "pop_front":
            if deq:
                print(deq.popleft())
            else:
                print("error")
        elif command == "pop_back":
            if deq:
                print(deq.pop())
            else:
                print("error")
        elif command == "front":
            if deq:
                print(deq[0])
            else:
                print("error")
        elif command == "back":
            if deq:
                print(deq[-1])
            else:
                print("error")
        elif command == "size":
            print(len(deq))
        elif command == "clear":
            deq.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    solve()