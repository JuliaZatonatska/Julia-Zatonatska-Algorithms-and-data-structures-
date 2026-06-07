import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    cursor = 2
    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2

        out_degree[u] += 1
        in_degree[v] += 1

    for i in range(1, n + 1):
        print(f"{in_degree[i]} {out_degree[i]}")


if __name__ == '__main__':
    solve()