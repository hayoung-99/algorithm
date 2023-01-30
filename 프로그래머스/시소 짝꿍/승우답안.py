from itertools import product
from heapq import heapify, heappop

distances = [2,3,4]

def solution(weights):
    ratios = list(set(map(lambda c: c[1]/c[0], product(distances, repeat=2))))
    heaped = list(weights)
    heapify(heaped)

    def step(_):
      cur = heappop(heaped)
      valid_weights = list(map(lambda r: cur * r, ratios))
      pairs = filter(lambda w: w in valid_weights, heaped)
      return len(list(pairs))

    pairs = list(map(step, weights))
    return sum(pairs)


print(solution([100,180,360,100,270]))
