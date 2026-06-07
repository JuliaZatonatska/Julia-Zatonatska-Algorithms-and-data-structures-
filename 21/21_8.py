import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    seen_edges = set()
    cursor = 2

    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2

        edge = (u, v)
        if edge in seen_edges:
            print("YES")
            return
        seen_edges.add(edge)

    print("NO")


if __name__ == '__main__':
    solve()