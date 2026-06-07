import sys


class TreeNode:
    def __init__(self, index: int, color: int):
        self.index = index
        self.color = color
        self.children = []
        self.size = 1
        self.heavy_child = None


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    nodes = [TreeNode(i, 0) for i in range(n + 1)]
    root_idx = 1

    cursor = 1
    for i in range(1, n + 1):
        p = int(input_data[cursor])
        c = int(input_data[cursor + 1])
        cursor += 2
        nodes[i].color = c
        if p == 0:
            root_idx = i
        else:
            nodes[p].children.append(nodes[i])

    order = []
    stack = [nodes[root_idx]]
    while stack:
        curr = stack.pop()
        order.append(curr)
        for child in curr.children:
            stack.append(child)

    for node in reversed(order):
        for child in node.children:
            node.size += child.size
            if node.heavy_child is None or child.size > node.heavy_child.size:
                node.heavy_child = child

    ans = [0] * (n + 1)
    color_count = [0] * (n + 1)
    distinct_colors = 0

    def add(node):
        nonlocal distinct_colors
        if color_count[node.color] == 0:
            distinct_colors += 1
        color_count[node.color] += 1
        for child in node.children:
            add(child)

    def remove(node):
        nonlocal distinct_colors
        color_count[node.color] -= 1
        if color_count[node.color] == 0:
            distinct_colors -= 1
        for child in node.children:
            remove(child)

    stack = [(nodes[root_idx], 0)]
    while stack:
        node, state = stack.pop()
        if state == 0:
            stack.append((node, 1))
            for child in node.children:
                if child != node.heavy_child:
                    stack.append((child, 2))
            if node.heavy_child:
                stack.append((node.heavy_child, 0))
        elif state == 1:
            if color_count[node.color] == 0:
                distinct_colors += 1
            color_count[node.color] += 1

            for child in node.children:
                if child != node.heavy_child:
                    add(child)
            ans[node.index] = distinct_colors
        elif state == 2:
            remove(node)

    print(*(ans[1:]))


if __name__ == '__main__':
    solve()