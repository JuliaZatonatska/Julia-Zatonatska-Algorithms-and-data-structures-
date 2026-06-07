import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = int(input_data[2])
    b = int(input_data[3])
    d = int(input_data[4])

    adj = [[] for _ in range(n + 1)]
    cursor = 5
    for _ in range(k):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2
        adj[u].append(v)

    visited = [False] * (n + 1)
    routes_count = 0

    def dfs(u, days):
        nonlocal routes_count
        if u == b:
            routes_count += 1
            return

        if days == d:
            return

        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v, days + 1)
        visited[u] = False

    dfs(a, 0)
    print(routes_count)


if __name__ == '__main__':
    solve()