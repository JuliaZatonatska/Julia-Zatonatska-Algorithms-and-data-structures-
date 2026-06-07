import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    str_a, str_b = input_data[0], input_data[1]

    if str_a == "0" or str_b == "0":
        print(0)
        return

    BASE = 1000000000
    SIZE = 9

    def to_blocks(s):
        blocks = []
        n = len(s)
        for i in range(n, 0, -SIZE):
            start = max(0, i - SIZE)
            blocks.append(int(s[start:i]))
        return blocks

    a = to_blocks(str_a)
    b = to_blocks(str_b)

    len_a, len_b = len(a), len(b)
    result = [0] * (len_a + len_b)

    for i in range(len_a):
        carry = 0
        val_a = a[i]
        for j in range(len_b):
            current = val_a * b[j] + result[i + j] + carry
            result[i + j] = current % BASE
            carry = current // BASE
        if carry:
            result[i + len_b] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    out = [str(result[-1])]
    for i in range(len(result) - 2, -1, -1):
        out.append(f"{result[i]:09d}")

    print("".join(out))


if __name__ == "__main__":
    solve()