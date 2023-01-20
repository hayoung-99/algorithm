from heapq import heappushpop, heappush


def solution(n, k, enemy):
    defeated_enemy = []
    skip_enemy = []

    def round(e):
        if len(skip_enemy) < k:
            heappush(skip_enemy, e)
        else:
            small_enemy = heappushpop(skip_enemy, e)
            heappush(defeated_enemy, small_enemy)

    for i, e in enumerate(enemy):
        if sum(defeated_enemy) <= n:
            round(e)
        else:
            return i - 1
    return len(enemy)
