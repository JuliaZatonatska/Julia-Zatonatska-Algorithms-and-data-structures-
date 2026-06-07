import sys

sys.setrecursionlimit(2000)


class EmployeeNode:
    def __init__(self, cost: int):
        self.cost = cost
        self.subordinates = []


def find_min_cost(node: EmployeeNode) -> int:
    if not node.subordinates:
        return node.cost
    return node.cost + min(find_min_cost(sub) for sub in node.subordinates)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    employees = [None] * (n + 1)
    subordinate_ids = {}

    cursor = 1
    for i in range(1, n + 1):
        cost = int(input_data[cursor])
        k = int(input_data[cursor + 1])

        employees[i] = EmployeeNode(cost)

        subs = []
        for j in range(k):
            subs.append(int(input_data[cursor + 2 + j]))
        subordinate_ids[i] = subs

        cursor += 2 + k

    for i in range(1, n + 1):
        for sub_id in subordinate_ids[i]:
            employees[i].subordinates.append(employees[sub_id])

    root = employees[1]
    print(find_min_cost(root))


if __name__ == '__main__':
    solve()