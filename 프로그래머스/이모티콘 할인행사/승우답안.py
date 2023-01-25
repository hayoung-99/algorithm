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

    # 판매액 구하는 로직은 아예 틀린듯

    answer = [len(plus_users), 0]
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
