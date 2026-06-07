import sys


class DirectoryNode:
    def __init__(self, name: str):
        self.name = name
        self.children = {}

    def insert(self, path_parts: list, index: int = 0) -> None:
        if index == len(path_parts):
            return

        part = path_parts[index]
        if part not in self.children:
            self.children[part] = DirectoryNode(part)

        self.children[part].insert(path_parts, index + 1)

    def print_tree(self, depth: int = -1) -> None:
        if depth >= 0:
            print(" " * depth + self.name)

        for child_name in sorted(self.children.keys()):
            self.children[child_name].print_tree(depth + 1)


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    root = DirectoryNode("")

    for i in range(1, n + 1):
        path = input_data[i].strip()
        if path:
            parts = path.split('\\')
            root.insert(parts)

    root.print_tree()


if __name__ == '__main__':
    solve()