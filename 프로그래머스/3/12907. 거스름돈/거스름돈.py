# import math

# def recursion(n, money, idx, curr):
#     global answer
    
#     rest_money = n - curr
    
#     if rest_money == 0:
#         answer += 1
#         return
    
#     if idx == len(money) - 1:
#         if rest_money % money[idx] == 0:
#             answer += 1
#         return
    
#     for i in range(math.floor(rest_money / money[idx]), -1, -1):
#         recursion(n, money, idx+1, i * money[idx] + curr)
        

# def solution(n, money):
#     global answer
#     answer = 0
    
#     recursion(n, money, 0, 0)
    
#     return answer


def solution(n, money):
    money.sort()
    
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    
    for currency in money:
        for i in range(currency, n+1):
            dp[i] += dp[i - currency]
        
    return dp[n]