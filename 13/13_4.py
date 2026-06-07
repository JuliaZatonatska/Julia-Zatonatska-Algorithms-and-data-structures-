import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    a = int(input_data[0])
    p = int(input_data[1])

    if a == 0:
        print(0)
        return

    stack = []

    while a > 0:
        remainder = a % p
        stack.append(remainder)
        a //= p

    result = []
    while stack:
        digit = stack.pop()
        if digit > 9:
            result.append(f"[{digit}]")
        else:
            result.append(str(digit))

    print("".join(result))


if __name__ == "__main__":
    solve()