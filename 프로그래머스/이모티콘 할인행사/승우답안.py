from itertools import filterfalse


def solution(users, emoticons):
    sum_emoticons = sum(emoticons)

    def user_max_plan(user):
        [ratio, budget] = user
        max_budget = int(budget / (1 - ratio / 100))
        if max_budget > sum_emoticons:
            return False
        return True

    valid_ratio = [10, 20, 30, 40]
    plus_users = list(filter(user_max_plan, users))
    purchase_users = list(filterfalse(user_max_plan, users))
    min_ratio = max(plus_users, key=lambda x: x[0])[0] if plus_users else 100
    ## 바로 윗줄 구하는 식을 좀 더 구현해야함
    print(min_ratio, purchase_users)

    def sum_of_purchase(ratio, emoticon):
        target_users = list(filter(lambda u: u[0] <= ratio, purchase_users))
        return int((1 - ratio / 100) * emoticon * len(target_users))

    def emoticon_plan(emoticon):
        valid_ratios = [r for r in valid_ratio if r > min_ratio]
        sum_func = lambda r: sum_of_purchase(r, emoticon)
        return max(list(map(sum_func, valid_ratios))) if valid_ratios else 0

    answer = [len(plus_users), max(list(map(emoticon_plan, emoticons)))]
    return answer


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(
    solution(
        [
            [40, 2900],
            [23, 10000],
            [11, 5200],
            [5, 5900],
            [40, 3100],
            [27, 9200],
            [32, 6900],
        ],
        [1300, 1500, 1600, 4900],
    )
)
