import sys
import math


def solve():
    input_data = sys.stdin.read().split()
    if not input_data or input_data[0] == '0':
        return

    cursor = 0
    num_elements = len(input_data)

    while cursor < num_elements:
        n = int(input_data[cursor])
        if n == 0:
            break
        cursor += 1

        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i] = int(input_data[cursor])
            y[i] = int(input_data[cursor + 1])
            cursor += 2

        INF = float('inf')
        min_dist_sq = [INF] * n
        visited = [False] * n

        min_dist_sq[0] = 0
        total_length = 0.0

        for _ in range(n):
            u = -1
            current_min_sq = INF
            for i in range(n):
                if not visited[i] and min_dist_sq[i] < current_min_sq:
                    current_min_sq = min_dist_sq[i]
                    u = i

            if u == -1:
                break

            visited[u] = True
            total_length += math.sqrt(current_min_sq)

            ux, uy = x[u], y[u]
            for v in range(n):
                if not visited[v]:
                    d_sq = (ux - x[v]) * (ux - x[v]) + (uy - y[v]) * (uy - y[v])
                    if d_sq < min_dist_sq[v]:
                        min_dist_sq[v] = d_sq

        print(f"{total_length:.2f}")


if __name__ == '__main__':
    solve()