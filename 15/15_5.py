import sys


class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None


class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        current = self.head
        first = True
        while current is not None:
            if not first:
                print(" ", end="")
            print(current.data, end="")
            first = False
            current = current.next
        print()

    def _print_reverse_recursive(self, node: [Node | None]) -> bool:
        if node is None:
            return True
        is_first = self._print_reverse_recursive(node.next)
        if not is_first:
            print(" ", end="")
        print(node.data, end="")
        return False

    def PrintReverse(self) -> None:
        self._print_reverse_recursive(self.head)
        print()


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    linked_list = List()

    for i in range(1, n + 1):
        linked_list.addToTail(int(input_data[i]))

    linked_list.Print()
    linked_list.PrintReverse()


if __name__ == "__main__":
    solve()