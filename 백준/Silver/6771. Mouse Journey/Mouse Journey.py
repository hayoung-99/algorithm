# =============== 입력 ===============
r, c = map(int, input().split())
k = int(input())

cats_pos = []
for _ in range(k):
    y, x = map(int, input().split())
    cats_pos.append((x, y))

# =============== main ===============
dp = [[0 for _ in range(r+1)] for _ in range(c+1)]
cats_map = [[0 for _ in range(r+1)] for _ in range(c+1)]
for x, y in cats_pos:
    cats_map[x][y] = 1

dp[1][1] = 1
for x in range(2, c+1):
    if cats_map[x][1]:
        break

    dp[x][1] = dp[x-1][1]

for y in range(2, r+1):
    if cats_map[1][y]:
        break

    dp[1][y] = dp[1][y-1]

for x in range(2, c+1):
    for y in range(2, r+1):
        if cats_map[x][y]:
            continue

        dp[x][y] = dp[x-1][y] + dp[x][y-1]

print(dp[c-1][r] + dp[c][r-1])
