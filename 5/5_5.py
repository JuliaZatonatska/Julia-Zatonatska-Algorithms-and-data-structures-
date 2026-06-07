import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    n = int(next(iterator))
    m = int(next(iterator))

    times = []
    curr_bus_time = 0

    for i in range(n):
        travel_time = int(next(iterator))
        k = int(next(iterator))

        for _ in range(k):
            arr_time = int(next(iterator))
            times.append(max(0, arr_time - curr_bus_time))

        curr_bus_time += travel_time

    times.sort()

    total_wait = 0
    max_workers = min(len(times), m)
    if max_workers > 0:
        total_wait = times[max_workers - 1]

    print(curr_bus_time + total_wait)


if __name__ == '__main__':
    solve()