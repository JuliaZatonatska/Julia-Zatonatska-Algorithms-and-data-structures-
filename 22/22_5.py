import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(n + 1)]
    cursor = 2

    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2
        adj[u].append(v)
        adj[v].append(u)

    k = int(input_data[cursor])
    cursor += 1

    dist = [-1] * (n + 1)
    queue = deque()

    for _ in range(k):
        start_node = int(input_data[cursor])
        cursor += 1
        dist[start_node] = 0
        queue.append(start_node)

    max_dist = 0
    last_node = queue[0] if queue else 1

    while queue:
        u = queue.popleft()
        current_dist = dist[u]

        if current_dist > max_dist:
            max_dist = current_dist
            last_node = u
        elif current_dist == max_dist and u < last_node:
            last_node = u

        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = current_dist + 1
                queue.append(v)

    print(max_dist)
    print(last_node)


if __name__ == '__main__':
    solve()