import copy

def solution(board):
    # DP
    DP = copy.deepcopy(board)
    max_length = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if x == 0 or y == 0:
                if board[x][y] == 1:
                    max_length = max(max_length, 1)
                continue
            
            if board[x][y] == 1:
                DP[x][y] = min(DP[x-1][y], DP[x][y-1], DP[x-1][y-1]) + 1
                max_length = max(max_length, DP[x][y])
                
    return max_length ** 2
