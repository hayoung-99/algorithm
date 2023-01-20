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

    iters = takewhile(lambda a: a <= n, accumulate(enemy, round))
    result = list(iters)
    if not result:
        return len(enemy)
    return len(result)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
