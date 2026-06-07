import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    dist = []
    cursor = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[cursor]))
            cursor += 1
        dist.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        print(*(dist[i]))


if __name__ == '__main__':
    solve()