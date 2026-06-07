import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    words = input_data[1:n + 1]

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if words[j] < words[min_idx]:
                min_idx = j
        words[i], words[min_idx] = words[min_idx], words[i]

    for word in words:
        print(word)


if __name__ == '__main__':
    solve()