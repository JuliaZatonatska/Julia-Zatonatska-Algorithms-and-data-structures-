import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    r = int(input_data[0])
    l = int(input_data[1])
    b = int(input_data[2])

    x = [int(val) for val in input_data[3:3 + r]]

    pref = [0] * (r + 1)
    for i in range(r):
        pref[i + 1] = pref[i] + x[i]

    def get_cost(i, j):
        mid = (i + j) // 2
        left_count = mid - i
        right_count = j - mid

        left_sum = pref[mid] - pref[i]
        right_sum = pref[j + 1] - pref[mid + 1]

        cost = (left_count * x[mid] - left_sum) + (right_sum - right_count * x[mid])
        return cost

    max_len = 0
    i = 0
    for j in range(r):
        while get_cost(i, j) > b:
            i += 1
        max_len = max(max_len, j - i + 1)

    print(max_len)


if __name__ == '__main__':
    solve()