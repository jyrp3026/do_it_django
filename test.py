def solution(i, j, k):
    return sum(str(n).count(str(k)) for n in range(i, j + 1))

print(solution(1, 13, 2))


def solution(array):
    counts = {}
    for n in array:
        counts[n] = counts.get(n, 0) + 1

    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]

    return modes[0] if len(modes) == 1 else -1

print(solution([1, 2, 3, 3, 3, 4]))  # 3
print(solution([1, 1, 2, 2]))         # -1
print(solution([1]))              