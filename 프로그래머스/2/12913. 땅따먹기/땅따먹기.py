def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    
    for col in range(len(land)):
        for row in range(4):
            if col == 0:
                dp[0][row] = land[0][row]
            else:
                for i in range(4):
                    if i != row:
                        dp[col][row] = max(dp[col][row], land[col][row] + dp[col-1][i])
                        
    answer = 0
    
    for i in dp[-1]:
        answer = max(answer, i)
        
    return answer