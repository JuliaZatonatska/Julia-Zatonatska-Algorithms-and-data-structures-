import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]

    for i in range(1, n):
        key = a[i]
        key_last_digit = key % 10
        j = i - 1

        while j >= 0:
            curr_last_digit = a[j] % 10

            if curr_last_digit > key_last_digit or (curr_last_digit == key_last_digit and a[j] > key):
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    print(*(a))


if __name__ == '__main__':
    solve()