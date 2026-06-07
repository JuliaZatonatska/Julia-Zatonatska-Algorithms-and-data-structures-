import sys


def check(d, intervals, n):
    count = 0
    curr_pos = -d

    for a, b in intervals:
        while max(a, curr_pos + d) <= b:
            curr_pos = max(a, curr_pos + d)
            count += 1
            if count >= n:
                return True
    return False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    intervals = []
    idx = 2
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        intervals.append((a, b))
        idx += 2

    intervals.sort()

    low = 1
    high = (intervals[-1][1] - intervals[0][0]) // (n - 1) + 1
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if check(mid, intervals, n):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)


if __name__ == '__main__':
    solve()