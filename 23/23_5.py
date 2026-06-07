import sys
import random

sys.setrecursionlimit(200000)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    adj = [[] for _ in range(n + 1)]

    uf = UnionFind(n)
    is_tree_edge = [False] * (m + 1)

    cursor = 2
    for i in range(1, m + 1):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        cursor += 2
        edges.append((u, v))

        if uf.union(u, v):
            is_tree_edge[i] = True
            adj[u].append((v, i))
            adj[v].append((u, i))

    edge_hash = [0] * (m + 1)
    node_xor = [0] * (n + 1)

    random.seed(42)
    for i in range(1, m + 1):
        if not is_tree_edge[i]:
            u, v = edges[i - 1]
            h = random.getrandbits(60)
            edge_hash[i] = h
            node_xor[u] ^= h
            node_xor[v] ^= h

    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        current_xor = node_xor[u]

        for v, edge_idx in adj[u]:
            if not visited[v]:
                child_xor = dfs(v)
                edge_hash[edge_idx] = child_xor
                current_xor ^= child_xor

        return current_xor

    dfs(1)

    k = int(input_data[cursor])
    cursor += 1

    output = []

    for _ in range(k):
        c = int(input_data[cursor])
        cursor += 1

        query_hashes = []
        for _ in range(c):
            e_idx = int(input_data[cursor])
            query_hashes.append(edge_hash[e_idx])
            cursor += 1

        connected = True
        num_hashes = len(query_hashes)

        for mask in range(1, 1 << num_hashes):
            subset_xor = 0
            for j in range(num_hashes):
                if (mask >> j) & 1:
                    subset_xor ^= query_hashes[j]
            if subset_xor == 0:
                connected = False
                break

        if connected:
            output.append("Connected")
        else:
            output.append("Disconnected")

    print("\n".join(output))


if __name__ == '__main__':
    solve()