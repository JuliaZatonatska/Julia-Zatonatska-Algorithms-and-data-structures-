import sys

sys.setrecursionlimit(100000)


class BinaryTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def insert_path(self, path: list, index: int, low: float, high: float) -> bool:
        if index == len(path):
            return True

        next_val = path[index]

        if not (low < next_val < high):
            return False

        if next_val < self.val:
            self.left = BinaryTreeNode(next_val)
            return self.left.insert_path(path, index + 1, low, self.val)
        else:
            self.right = BinaryTreeNode(next_val)
            return self.right.insert_path(path, index + 1, self.val, high)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    path = [int(x) for x in input_data]

    root = BinaryTreeNode(path[0])

    if root.insert_path(path, 1, float('-inf'), float('+inf')):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    solve()