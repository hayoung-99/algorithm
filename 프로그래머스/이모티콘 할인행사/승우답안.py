from itertools import product, chain
from functools import reduce

valid_discount_ratios = [10, 20, 30, 40]

def calculate_user(user, emoticons):
    ratio, budget = user
    purchase_emoticons = list(filter(lambda e: e[0] >= ratio, emoticons))
    if not purchase_emoticons:
        return 1
    def cost_func(emoticon):
        cost = round(emoticon[1] * (100 - emoticon[0]) / 100)
        return cost
    purchase_cost = sum(map(cost_func, purchase_emoticons))
    return 0 if purchase_cost >= budget else purchase_cost

def accumulate_user(acc, cost):
    if not cost:
        return (acc[0] + 1, acc[1])
    elif cost == 1:
        return acc
    else:
        return (acc[0], acc[1]+ cost)

def calculate_case(case, users):
    emoticons = list(case)
    user_func = lambda u: calculate_user(u, emoticons)
    user_costs = list(map(user_func, users))
    return reduce(accumulate_user, user_costs, (0,0))


def solution(users, emoticons):
    len_emoticon = len(emoticons)
    emoticon_ratio_cases = product(valid_discount_ratios, repeat=len_emoticon)
    cases = map(lambda c: zip(c, emoticons), emoticon_ratio_cases)
    case_func = lambda c: calculate_case(c, users)
    results = map(case_func, cases)
    answer = sorted(chain(results), key=lambda r: (r[0], r[1])).pop()
    return answer


