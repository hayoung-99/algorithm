def solution(n, k, enemy):
    length = len(enemy)
    if k > length:
        return length

    def calculate(index):
        sum_enemy = sum(enemy[: index + 1])
        max_sorted_enemy = sorted(enemy[: index + 1], reverse=True)
        sum_skip_enemy = sum(max_sorted_enemy[:k])
        defeated_enemy = sum_enemy - sum_skip_enemy
        residul_soldier = n - defeated_enemy
        return index, 0 if residul_soldier >= 0 else 1

    sort_func = lambda x: (x[1], -x[0])
    index, _ = sorted([calculate(i) for i in range(length)], key=sort_func)[0]
    return index + 1
