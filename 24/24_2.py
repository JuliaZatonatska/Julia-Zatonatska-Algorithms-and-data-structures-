import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    grid = [list(row) for row in input_data[1:n + 1]]

    start = None
    end = None

    for r in range(n):
        for c in range(n):
            if grid[r][c] == '@':
                start = (r, c)
            elif grid[r][c] == 'X':
                end = (r, c)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    visited[start[0]][start[1]] = True
    found = False

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            found = True
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] == '.' or grid[nr][nc] == 'X':
                    visited[nr][nc] = True
                    parent[nr][nc] = (r, c)
                    queue.append((nr, nc))

    if not found:
        print("N")
        return

    print("Y")
    curr = end
    while curr != start:
        r, c = curr
        if grid[r][c] == 'X' or grid[r][c] == '.':
            grid[r][c] = '+'
        curr = parent[r][c]

    for row in grid:
        print("".join(row))


if __name__ == '__main__':
    solve()