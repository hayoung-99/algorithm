n = int(input())

dp = [0 for _ in range(n + 1)]  # 인덱스 0은 쓰지 않는다.
dp[1] = 0

for i in range(2, n+1):
    temp = []
    if i % 2 == 0:
        temp.append(dp[i // 2])
    if i % 3 == 0:
        temp.append(dp[i // 3])
    temp.append(dp[i-1])

    dp[i] = min(temp) + 1

print(dp[n])
