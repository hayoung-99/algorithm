from itertools import accumulate


def solution(n, k, enemy):
    length = len(enemy)
    if k >= length:
        return length

    def calculate(value: tuple):
        index, sum_enemy = value
        max_sorted_enemy = sorted(enemy[: index + 1], reverse=True)
        sum_skip_enemy = sum(max_sorted_enemy[:k])
        defeated_enemy = sum_enemy - sum_skip_enemy
        residul_soldier = n - defeated_enemy
        return index if residul_soldier >= 0 else 0

    index = max(map(calculate, enumerate(accumulate(enemy))))
    return index + 1
