import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    unique_edges = set()
    cursor = 2

    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2

        if u != v:
            if u > v:
                u, v = v, u
            unique_edges.add((u, v))

    required_edges = n * (n - 1) // 2

    if len(unique_edges) == required_edges:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()