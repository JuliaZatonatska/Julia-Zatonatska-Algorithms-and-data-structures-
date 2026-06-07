import sys

sys.setrecursionlimit(300000)


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

    visited = [0] * (n + 1)
    order = []
    possible = True

    def dfs(u):
        nonlocal possible
        if not possible:
            return

        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 1:
                possible = False
                return
            elif visited[v] == 0:
                dfs(v)
                if not possible:
                    return

        visited[u] = 2
        order.append(u)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            if not possible:
                print("-1")
                return

    order.reverse()
    print(*(order))


if __name__ == '__main__':
    solve()