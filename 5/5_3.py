import sys


def check(dist, coords, k):
    count = 1
    last_pos = coords[0]
    for i in range(1, len(coords)):
        if coords[i] - last_pos >= dist:
            count += 1
            last_pos = coords[i]
            if count >= k:
                return True
    return False


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    coords = [int(x) for x in data[2:n + 2]]

    low = 0
    high = coords[-1] - coords[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if check(mid, coords, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)


if __name__ == '__main__':
    solve()