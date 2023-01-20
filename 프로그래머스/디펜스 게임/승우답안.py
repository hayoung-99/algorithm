from itertools import accumulate, takewhile
from heapq import heappushpop, heappush


def solution(n, k, enemy):
    skip_enemy = []

    def round(sum_enemy, e):
        if len(skip_enemy) < k:
            heappush(skip_enemy, e)
            return sum_enemy
        else:
            small_enemy = heappushpop(skip_enemy, e)
            return small_enemy + sum_enemy

    iters = takewhile(lambda a: a <= n, accumulate(enemy, round, initial=0))
    result = list(iters)
    if not result:
        return len(enemy)
    return len(result) - 1
