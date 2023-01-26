plusUsers, totalPrice = 0, 0


def getPrices(users, emoticons, prices, i):
    global plusUsers, totalPrice

    # 모든 emoticons를 돌았다면
    if i == len(emoticons):
        curPlusUsers = 0
        curTotalPrice = 0
        for user in users:
            tempPrice = 0
            discount = math.floor(user[0] / 10) * 10
            limit = user[1]

            for k in range(discount, 41, 10):
                tempPrice += sum(prices[k])

            if limit >= result:
                curPlusUsers += 1
            else:
                curTotalPrice += tempPrice

        if plusUsers < curPlusUsers:
            plusUsers = curPlusUsers
            totalPrice = curTotalPrice

        elif plusUsers == curPlusUsers:
            if totalPrice < curTotalPrice:
                totalPrice = curTotalPrice

        return

    # 10%

    # 20%

    # 30%

    # 40%


def solution(users, emoticons):
    prices = {}





