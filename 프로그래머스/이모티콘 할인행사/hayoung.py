import math

plusUsers, totalPrice = 0, 0


def getPrices(users, emoticons, prices, i):
    global plusUsers, totalPrice

    # 모든 emoticons를 돌았다면
    if i == len(emoticons):
        curPlusUsers = 0
        curTotalPrice = 0
        for user in users:
            tempPrice = 0
            discount = math.ceil(user[0] / 10) * 10
            limit = user[1]

            if discount == 0:
                discount = 10

            for k in range(discount, 41, 10):
                tempPrice += sum(prices[k])

            if limit <= tempPrice:
                curPlusUsers += 1
            else:
                curTotalPrice += tempPrice

        # plusUsers, totalPrice 업데이트
        if plusUsers < curPlusUsers:
            plusUsers = curPlusUsers
            totalPrice = curTotalPrice

        elif plusUsers == curPlusUsers:
            if totalPrice < curTotalPrice:
                totalPrice = curTotalPrice

        return

    # 10% ~ 40% 할인 적용
    for d in range(10, 41, 10):
        price = int(emoticons[i] / 100) * (100 - d)
        prices[d].append(price)
        getPrices(users, emoticons, prices, i + 1)
        prices[d].pop()  # 42줄의 append를 되돌리기


def solution(users, emoticons):
    prices = {
        10: [],
        20: [],
        30: [],
        40: []
    }

    getPrices(users, emoticons, prices, 0)

    return [plusUsers, totalPrice]