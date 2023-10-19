T = int(input())

dp = [0 for _ in range(12)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

curr_dp = 2

for _ in range(T):
    n = int(input())

    if n > curr_dp:
        # 새롭게 dp 구하기
        while curr_dp <= n:
            curr_dp += 1
            dp[curr_dp] = dp[curr_dp - 1] + dp[curr_dp - 2] + dp[curr_dp - 3]

    print(dp[n])
