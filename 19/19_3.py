import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [0] + [int(x) for x in input_data[1:n+1]]

    for i in range(1, n + 1):
        if 2 * i <= n:
            if a[i] > a[2 * i]:
                print("NO")
                return
        if 2 * i + 1 <= n:
            if a[i] > a[2 * i + 1]:
                print("NO")
                return

    print("YES")

if __name__ == '__main__':
    solve()