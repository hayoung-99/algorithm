from itertools import product, filterfalse


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

    ratio_cases = list(product(valid_ratio, repeat=len(emoticons)))

    def emoticon_cost(pair, case):
        index = pair[0]
        emoticon = pair[1]
        ratio = case[index]
        target_user = len(
            list(filter(lambda u: u[0] <= ratio and not user_max_plan(u), users))
        )
        return int(emoticon * (1 - ratio / 100)) * target_user

    def sum_of_emoticon(case):
        sum_func = lambda e: emoticon_cost(e, case)
        return sum(map(sum_func, enumerate(emoticons)))

    valid_case = max(ratio_cases, key=lambda c: sum_of_emoticon(c))

    # 판매액 구하는 로직은 아예 틀린듯

    answer = [len(plus_users), valid_case]
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
