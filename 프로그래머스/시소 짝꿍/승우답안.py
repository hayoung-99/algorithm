from functools import reduce
from math import comb

distances = [2,3,4]

def count_same(acc, weight):
    if weight >= 2:
      return acc + comb(weight, 2)
    return acc

def solution(weights):
    answer = 0
    weight_maps = {}
    ratios = [(3,2), (4,3), (4,2)]

    def count(weight):
      if weight not in weight_maps:
        weight_maps[weight] = 1
      else:
        weight_maps[weight] += 1

    list(map(count, weights))

    def calculate_ratio(ratio, weight):
        cur = weight * ratio[0] / ratio[1]
        if cur in weight_maps:
          return weight_maps[cur]
        return 0

    def count_other(weight):
      acc_func = lambda r: calculate_ratio(r, weight)
      return sum(map(acc_func, ratios))

    answer += reduce(count_same, weight_maps.values(), answer)
    answer += sum(map(count_other, weights))
    return answer



print(solution([100,180,360,100,270]))
