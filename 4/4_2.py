import sys


def solve():
    c = float(sys.stdin.read().strip())

    left = 0.0
    right = 100000.0

    for _ in range(100):
        mid = (left + right) / 2
        if mid * mid + mid ** 0.5 >= c:
            right = mid
        else:
            left = mid

    print(f"{left:.9f}")


if __name__ == "__main__":
    solve()
