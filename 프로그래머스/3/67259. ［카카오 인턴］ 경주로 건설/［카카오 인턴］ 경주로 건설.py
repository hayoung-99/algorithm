import sys
from collections import deque

COST_STRAIGHT = 100
COST_CORNER = 600
answer = sys.maxsize


def inRange(x, y, n):
    return 0 <= x < n and 0 <= y < n


# # 1) BFS로 풀이
# def BFS(x, y, board):
#     global answer 
    
#     # initial
#     n = len(board)
#     q = deque()
#     cost_board = [[-1 for _ in range(n)] for _ in range(n)]
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     # (0, 0) 방문
#     visited[x][y] = 1
#     for dx, dy in directions:
#         if inRange(dx, dy, n) and board[dx][dy] == 0:
#             q.append((dx, dy, COST_STRAIGHT, (dx, dy)))
#             visited[dx][dy] = 1
#             cost_board[dx][dy] = COST_STRAIGHT
    
#     while q:
#         x, y, cost, direction = q.popleft()
        
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if inRange(nx, ny, n) and board[nx][ny] == 0:
#                 curr_cost = cost + COST_STRAIGHT if (dx, dy) == direction else cost + COST_CORNER
#                 if not visited[nx][ny] or cost_board[nx][ny] + 400 >= curr_cost:
#                     q.append((nx, ny, curr_cost, (dx, dy)))
#                     cost_board[nx][ny] = curr_cost
#                     visited[nx][ny] = 1
                    
#                     if nx == n - 1 and ny == n - 1:
#                         answer = min(answer, curr_cost)


# def solution(board):
#     global answer
    
#     n = len(board)
#     BFS(0, 0, board)
    
#     return answer
    
    
# 2) DFS로 풀이
def DFS(x, y, direction, cost, board, cost_board):
    global answer

    board[x][y] = 1  # 방문
    if cost_board[x][y] == -1 or cost_board[x][y] + 400 >= cost:
        cost_board[x][y] = cost
    else :
        # 현재는 더 cost가 적더라도 최적의 해가 아닐 수 있음
        # 예를 들어 앞서 다른 탐색에서 구한 cost1이 있고, 현재 새로 구한 cost2가 있다고 하자.
        # 지금은 cost1 < cost2이지만, cost1 + 600 > cost2 + 100인 경우가 있을 수 있다.
        # 따라서 두 식을 계산하면 cost1 < cost2 <= cost1 + 400인 cost2가 존재한다면 cost를 업데이트하고, 아니라면 얼리 리턴한다.
        return

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
    
    n = len(board)
    cost_board = [[-1 for _ in range(n)] for _ in range(n)]

    # 시작점 -> 오른쪽 진행 or 아래 진행
    board[0][0] = 1
    cost_board[0][0] = 0
    directions = [(0, 1), (1, 0)]
    for d in directions:
        nx, ny = d
        if board[nx][ny] == 0:
            DFS(nx, ny, d, COST_STRAIGHT, board, cost_board)
            board[nx][ny] = 0  # 다른 탐색을 위해 rollback

    return answer