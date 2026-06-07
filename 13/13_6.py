import sys


def solve():
    line = sys.stdin.read().strip()
    if not line:
        return

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []

    for char in reversed(line):
        if char.isalpha():
            stack.append((char, 3))
        else:
            op = char
            left_expr, left_prec = stack.pop()
            right_expr, right_prec = stack.pop()

            op_prec = precedence[op]

            if left_prec < op_prec:
                left_expr = f"({left_expr})"

            if right_prec < op_prec:
                right_expr = f"({right_expr})"
            elif right_prec == op_prec and op in ("-", "/"):
                right_expr = f"({right_expr})"

            new_expr = f"{left_expr}{op}{right_expr}"
            stack.append((new_expr, op_prec))

    print(stack[0][0])


if __name__ == "__main__":
    solve()