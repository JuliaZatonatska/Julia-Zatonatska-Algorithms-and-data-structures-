import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    cursor = 1
    hanging_vertices_count = 0

    for i in range(n):
        degree = 0
        for j in range(n):
            if int(input_data[cursor]) == 1:
                degree += 1
            cursor += 1

        if degree == 1:
            hanging_vertices_count += 1

    print(hanging_vertices_count)


if __name__ == '__main__':
    solve()