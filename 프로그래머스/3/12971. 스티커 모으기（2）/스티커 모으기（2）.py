def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    # dp1: sticker[0]를 포함할 경우 -> sticker[i - 2]까지만 탐색
    # 또는 dp1[1]에서 sticker[0]을 선택하지 않을 경우 -> dp2에서 sticker[i - 1]까지 탐색 
    dp1 = [0] * len(sticker)
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        # 현재 sitkcer[i]를 선택하거나 혹은 선택하지 않거나의 max 값을 현재 dp[i]에 저장
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # dp2: sticker[0]를 선택하지 않음 -> sticker[i - 1]까지 탐색
    dp2 = [0] * len(sticker)
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        # 현재 sitkcer[i]를 선택하거나 혹은 선택하지 않거나의 max 값을 현재 dp[i]에 저장
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    return max(max(dp1), max(dp2))