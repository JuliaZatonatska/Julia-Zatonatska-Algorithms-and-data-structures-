import sys


def solve():
    stack = []

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue

        command = parts[0]

        if command == "push":
            n = parts[1]
            stack.append(n)
            print("ok")
        elif command == "pop":
            if stack:
                print(stack.pop())
            else:
                print("error")
        elif command == "back":
            if stack:
                print(stack[-1])
            else:
                print("error")
        elif command == "size":
            print(len(stack))
        elif command == "clear":
            stack.clear()
            print("ok")
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    solve()