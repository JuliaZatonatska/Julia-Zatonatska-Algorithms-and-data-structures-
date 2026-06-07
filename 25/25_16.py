import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    cursor = 1
    for i in range(n):
        for j in range(n):
            val = int(input_data[cursor])
            cursor += 1
            if i == j:
                dist[i][j] = 0
                if val < 0:
                    dist[i][j] = val
            elif val != 0:
                dist[i][j] = val

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < INF and dist[k][j] < INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] != INF:
                ans[i][j] = 1

    for k in range(n):
        if dist[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        ans[i][j] = 2

    for i in range(n):
        print(*(ans[i]))


if __name__ == '__main__':
    solve()