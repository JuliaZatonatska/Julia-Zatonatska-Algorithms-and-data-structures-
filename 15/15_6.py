import sys


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        if not self.head or not self.head.next or k == 0:
            return

        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return

        current.next = self.head

        steps_to_new_tail = length - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        new_tail.next = None
        self.tail = new_tail

    def Print(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    initial_elements = [int(x) for x in input_data[1:n + 1]]
    k_queries = [int(x) for x in input_data[n + 1:]]

    linked_list = List()
    for val in initial_elements:
        linked_list.AddToTail(val)

    for k in k_queries:
        linked_list.RotateRight(k)
        linked_list.Print()


if __name__ == '__main__':
    main()