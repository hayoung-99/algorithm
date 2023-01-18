from time import time
from random import randint

enemy = [randint(1, 1000000) for x in range(1000000)]
n = 1000000000
k = 500000


def solution(n, k, enemy):
    length = len(enemy)
    if k >= length:
        return length

    def calculate(index):
        sum_enemy = sum(enemy[: index + 1])
        max_sorted_enemy = sorted(enemy[: index + 1], reverse=True)
        sum_skip_enemy = sum(max_sorted_enemy[:k])
        defeated_enemy = sum_enemy - sum_skip_enemy
        residul_soldier = n - defeated_enemy
        return index if residul_soldier >= 0 else 0

    index = sorted(map(calculate, range(k, length)), reverse=True)[0]
    return index + 1


s = time()
solution(n, k, enemy)
print(time() - s)
