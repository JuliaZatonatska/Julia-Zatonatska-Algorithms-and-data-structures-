import sys


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = None

    def Insert(self, val: int) -> None:
        def _insert(node: TreeNode, value: int) -> TreeNode:
            if not node:
                return TreeNode(value)
            if value < node.val:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.head = _insert(self.head, val)

    def IsSameTree(self, p: 'Tree') -> int:
        def _check(n1: TreeNode, n2: TreeNode) -> bool:
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            return _check(n1.left, n2.left) and _check(n1.right, n2.right)

        return 1 if _check(self.head, p.head) else 0


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr1 = [int(x) for x in input_data[1:n + 1]]

    m = int(input_data[n + 1])
    arr2 = [int(x) for x in input_data[n + 2:n + 2 + m]]

    tree1 = Tree()
    for x in arr1:
        tree1.Insert(x)

    tree2 = Tree()
    for x in arr2:
        tree2.Insert(x)

    print(tree1.IsSameTree(tree2))


if __name__ == '__main__':
    solve()