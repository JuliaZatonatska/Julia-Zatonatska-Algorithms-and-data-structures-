import sys

sys.setrecursionlimit(200000)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    robots = []
    idx = 1
    for _ in range(n):
        robots.append((int(input_data[idx]), int(input_data[idx+1])))
        idx += 2
    sorted_robots = merge_sort(robots)
    print('\n'.join(f"{m} {a}" for m, a in sorted_robots))

if __name__ == '__main__':
    solve()