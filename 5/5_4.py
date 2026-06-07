import sys


def check(length, ropes, k):
    if length == 0:
        return True
    count = 0
    for rope in ropes:
        count += rope // length
    return count >= k


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    ropes = []
    for i in range(2, n + 2):
        ropes.append(int(input_data[i]))

    low = 1
    high = max(ropes)
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if check(mid, ropes, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)


if __name__ == '__main__':
    solve()