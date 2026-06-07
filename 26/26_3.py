import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    cursor = 1

    for _ in range(t):
        n = int(input_data[cursor])
        m = int(input_data[cursor + 1])
        p = int(input_data[cursor + 2])
        q = int(input_data[cursor + 3])
        cursor += 4

        target_w = None
        adj = [[] for _ in range(n + 1)]

        for _ in range(m):
            u = int(input_data[cursor])
            v = int(input_data[cursor + 1])
            w = int(input_data[cursor + 2])
            cursor += 3

            if (u == p and v == q) or (u == q and v == p):
                target_w = w
            else:
                adj[u].append((v, w))
                adj[v].append((u, w))

        if target_w is None:
            print("NO")
            continue

        visited = [False] * (n + 1)
        queue = [p]
        visited[p] = True
        connected_with_smaller_edges = False

        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1

            if u == q:
                connected_with_smaller_edges = True
                break

            for v, w in adj[u]:
                if w < target_w and not visited[v]:
                    visited[v] = True
                    queue.append(v)

        if connected_with_smaller_edges:
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    solve()