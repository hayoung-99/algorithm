from itertools import combinations, product

distances = [2,3,4]

def calculate_weight(weight_pair, distance_cases):
  w1, w2 = weight_pair
  def cal_func(d_pair):
    d1, d2 = d_pair
    return w1 * d1 == w2 * d2
  return True if list(filter(cal_func, distance_cases)) else False

def solution(weights):
    distance_cases = list(product(distances, repeat=2))
    sets = combinations(weights, 2)
    cal_func= lambda p: calculate_weight(p, distance_cases)
    answer = len(list(filter(cal_func, sets)))
    return answer


solution([100,180,360,100,270])