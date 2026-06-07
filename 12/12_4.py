import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break

        while idx < len(input_data):
            if input_data[idx] == "0":
                idx += 1
                break

            target = []
            for _ in range(n):
                target.append(int(input_data[idx]))
                idx += 1

            stack = []
            current_wagon = 1
            possible = True

            for required in target:
                while current_wagon <= n and (
                    not stack or stack[-1] != required
                ):
                    stack.append(current_wagon)
                    current_wagon += 1

                if stack and stack[-1] == required:
                    stack.pop()
                else:
                    possible = False
                    break

            if possible:
                print("Yes")
            else:
                print("No")

        print("")


if __name__ == "__main__":
    solve()