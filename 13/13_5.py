import sys


def solve():
    line = sys.stdin.read().strip()

    if not line:
        print("yes")
        return

    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}

    for char in line:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack or stack[-1] != brackets[char]:
                print("no")
                return
            stack.pop()

    if not stack:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    solve()