import sys


class BinaryTreeNode:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val: str) -> None:
        if val < self.val:
            if self.left is None:
                self.left = BinaryTreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(val)
            else:
                self.right.insert(val)

    def pre_order(self, result: list) -> None:
        result.append(self.val)
        if self.left:
            self.left.pre_order(result)
        if self.right:
            self.right.pre_order(result)


def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    current_tree_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == '*':
            if current_tree_lines:
                reversed_lines = reversed(current_tree_lines)
                root = None

                for r_line in reversed_lines:
                    for char in r_line:
                        if root is None:
                            root = BinaryTreeNode(char)
                        else:
                            root.insert(char)

                if root:
                    res = []
                    root.pre_order(res)
                    print("".join(res))

                current_tree_lines = []
        else:
            current_tree_lines.append(line)


if __name__ == '__main__':
    solve()