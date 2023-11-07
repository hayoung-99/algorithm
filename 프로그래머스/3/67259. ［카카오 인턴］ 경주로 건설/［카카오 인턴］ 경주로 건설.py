import sys

COST_STRAIGHT = 100
COST_CORNER = 600

def inRange(x, y, n):
    return 0 <= x < n and 0 <= y < n


def DFS(x, y, direction, cost, board, cost_board):
    global answer
    
    board[x][y] = 1  # 방문
    # cost_board[x][y] = cost
    if cost_board[x][y] == -1 :
        cost_board[x][y] = cost
    else :
        if cost_board[x][y] + 400 < cost:
            return
        else : 
            cost_board[x][y] = cost
    
    # 도착
    if x == len(board) - 1 and y == len(board) - 1:
        answer = min(answer, cost)
        return
    
    # 갈 수 있는 길로 탐색 이어나가기
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        
        if inRange(nx, ny, len(board)) and board[nx][ny] == 0:
            # 다음 cost 구하기
            if direction == d:
                next_cost = cost + COST_STRAIGHT
            else:
                next_cost = cost + COST_CORNER
                        
            DFS(nx, ny, d, next_cost, board, cost_board)
            board[nx][ny] = 0  # 다른 탐색을 위해 rollback
        

def solution(board):
    global answer
    
    answer = sys.maxsize
    n = len(board)
    
    cost_board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # 시작점 -> 오른쪽 진행 or 아래 진행
    directions = [(0, 1), (1, 0)]
    for d in directions:
        nx, ny = d
        if board[nx][ny] == 0:
            DFS(nx, ny, d, COST_STRAIGHT, board, cost_board)
            board[nx][ny] = 0
    
    return answer




# cost = 99999999999

# def DFS(board, curmoney,direct,x,y, length, waycost) :
#     global cost
#     board[x][y] = 1
#     if waycost[x][y] == -1 :
#         waycost[x][y] = curmoney
#     else :
#         if waycost[x][y]+400 < curmoney :
#             return
#         else : 
#             waycost[x][y] = curmoney
#     if (x, y) == (length-1,length-1) :
#         if cost>curmoney :
#             cost = curmoney
#         return
#     direction = [(1,0),(0,1),(-1,0),(0,-1)]
#     for d in direction :
#         newx = x+d[0]
#         newy = y +d[1]
#         if max(newx,newy)<length and min(newx,newy) >=0 and board[newx][newy] == 0:
#             newcurmoney = curmoney + 100 if direct == d else curmoney + 600
#             DFS(board, newcurmoney, d, newx,newy, length, waycost)
#             board[newx][newy] = 0

# def solution(board):
#     global cost
#     board[0][0]=1
#     direction = [(1,0),(-1,0),(0,1),(0,-1)]
#     length = len(board)
#     waycost = [[-1 for i in range(length)] for i in range(length)]
#     waycost[0][0] = 0
#     for d in direction :
#         newx = d[0]
#         newy = d[1]
#         if max(newx, newy) < length and min(newx, newy) >= 0 and board[newx][newy] == 0:
#             DFS(board, 100, d, newx, newy, length, waycost)
#             board[newx][newy] = 0
#     return cost