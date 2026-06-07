import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    n = int(input_data[1])
    grid = [list(row) for row in input_data[2:m + 2]]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    components_count = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '#':
                components_count += 1
                stack = [(r, c)]
                grid[r][c] = '.'

                while stack:
                    curr_r, curr_c = stack.pop()
                    for i in range(4):
                        nr, nc = curr_r + dr[i], curr_c + dc[i]
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '#':
                            grid[nr][nc] = '.'
                            stack.append((nr, nc))

    print(components_count)


if __name__ == '__main__':
    solve()