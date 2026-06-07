import sys


def backtrack(n, k, current, used, result):
    if len(current) == k:
        result.append(" ".join(map(str, current)))
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            current.append(i)
            backtrack(n, k, current, used, result)
            current.pop()
            used[i] = False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    result = []
    used = [False] * (n + 1)

    backtrack(n, k, [], used, result)

    print("\n".join(result))


if __name__ == '__main__':
    solve()