import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    INF = float('inf')
    dist = []
    cursor = 1

    for i in range(n):
        row = []
        for j in range(n):
            val = int(input_data[cursor])
            cursor += 1
            if val == -1 and i != j:
                row.append(INF)
            else:
                row.append(val)
        dist.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    max_dist = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != INF and dist[i][j] > max_dist:
                max_dist = dist[i][j]

    print(max_dist)


if __name__ == '__main__':
    solve()