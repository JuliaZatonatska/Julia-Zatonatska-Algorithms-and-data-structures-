import sys


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.id_to_pos = {}

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.id_to_pos[self.heap[i][0]] = i
        self.id_to_pos[self.heap[j][0]] = j

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][1] > self.heap[parent][1]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while 2 * idx + 1 < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = left
            if right < n and self.heap[right][1] > self.heap[left][1]:
                largest = right
            if self.heap[largest][1] > self.heap[idx][1]:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def add(self, item_id, priority):
        self.heap.append((item_id, priority))
        idx = len(self.heap) - 1
        self.id_to_pos[item_id] = idx
        self._sift_up(idx)

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        item_id, priority = self.heap.pop()
        del self.id_to_pos[item_id]
        if self.heap:
            self._sift_down(0)
        return item_id, priority

    def change(self, item_id, new_priority):
        if item_id not in self.id_to_pos:
            return
        idx = self.id_to_pos[item_id]
        old_priority = self.heap[idx][1]
        self.heap[idx] = (item_id, new_priority)
        if new_priority > old_priority:
            self._sift_up(idx)
        else:
            self._sift_down(idx)


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    pq = PriorityQueue()
    output = []

    for line in input_data:
        parts = line.strip().split()
        if not parts:
            continue

        command = parts[0]
        if command == "ADD":
            item_id = parts[1]
            priority = int(parts[2])
            pq.add(item_id, priority)
        elif command == "POP":
            item_id, priority = pq.pop()
            output.append(f"{item_id} {priority}")
        elif command == "CHANGE":
            item_id = parts[1]
            new_priority = int(parts[2])
            pq.change(item_id, new_priority)

    print("\n".join(output))


if __name__ == '__main__':
    solve()