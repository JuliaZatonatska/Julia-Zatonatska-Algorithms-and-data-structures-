import sys

sys.setrecursionlimit(2000)


def solve_cd():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    while True:
        try:
            N = int(next(iterator))
            num_tracks = int(next(iterator))

            tracks = []
            for i in range(num_tracks):
                tracks.append((int(next(iterator)), i))

        except StopIteration:
            break

        tracks.sort(key=lambda x: x[0], reverse=True)

        suffix_sums = [0] * (num_tracks + 1)
        for i in range(num_tracks - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + tracks[i][0]

        best_sum = -1
        found_exact = False

        def brute_force(index, current_sum):
            nonlocal best_sum, found_exact

            if found_exact:
                return

            if current_sum > best_sum:
                best_sum = current_sum
                if best_sum == N:
                    found_exact = True
                    return

            if index == num_tracks:
                return

            if current_sum + suffix_sums[index] <= best_sum:
                return

            weight, _ = tracks[index]
            if current_sum + weight <= N:
                brute_force(index + 1, current_sum + weight)

            brute_force(index + 1, current_sum)

        brute_force(0, 0)

        print(f"sum:{best_sum}")


if __name__ == "__main__":
    solve_cd()