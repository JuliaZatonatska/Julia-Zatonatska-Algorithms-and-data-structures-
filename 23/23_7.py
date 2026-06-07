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
        adj[v].append(u)

    visited = [False] * (n + 1)
    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            stack = [i]
            visited[i] = True

            while stack:
                u = stack.pop()
                component.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)

            components.append(component)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(*(comp))


if __name__ == '__main__':
    solve()