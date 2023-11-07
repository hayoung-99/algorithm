import heapq

def inRange(x, y, r):
    return 0 <= x < r and 0 <= y < r


def solution(board):
    mapper = {
        'top': 0,
        'right': 1,
        'bottom': 2,
        'left': 3
    }
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    bfs_map = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    q = []
    
    # 출발점에서 오른쪽 / 아래 진행
    if board[0][1] == 0:
        bfs_map[0][1] = (0, 1, 1, [mapper['right']])
        heapq.heappush(q, bfs_map[0][1])  # (x, y, total_cost, direction)
    if board[1][0] == 0:
        bfs_map[0][1] = (1, 0, 1, [mapper['bottom']])
        heapq.heappush(q, bfs_map[0][1])
        
    while q:
        x, y, cost, directions = heapq.heappop(q)
        # print(f"현 지점 {x}, {y}")
        for dx, dy in zip(dxs, dys):
            if dx == 1:
                curr_direction = 'bottom'
            elif dx == -1:
                curr_direction = 'top'
            else:
                if dy == 1:
                    curr_direction = 'right'
                else:
                    curr_direction = 'left'
                    
            if inRange(x + dx, y + dy, len(board)) and board[x + dx][y + dy] == 0:
                if x + dx == 0 and y + dy == 0:
                    continue
                for d in directions:
                    # 직선 도로 or 코너 도로 => cost 업데이트
                    if d == 0 or d == 2:
                        if dx == -1 or dx == 1:
                            curr_cost = cost + 1
                        else:
                            curr_cost = cost + 6
                            
                    else:
                        if dy == 1 or dy == -1:
                            curr_cost = cost + 1
                        else:
                            curr_cost = cost + 6
                            
                    if bfs_map[x + dx][y + dy] == 0:
                        # print(f"(1) 기존 방향 {d}, 가려는 방향 {curr_direction} cost={curr_cost}")
                        bfs_map[x + dx][y + dy] = (x + dx, y + dy, curr_cost, [mapper[curr_direction]])
                        heapq.heappush(q, bfs_map[x + dx][y + dy])
                    else:
                        prev_cost = bfs_map[x + dx][y + dy][2]
                        if prev_cost >= curr_cost:
                            # print(f"(2) 기존 방향 {d}, 가려는 방향 {curr_direction} cost={curr_cost}")
                            bfs_map[x + dx][y + dy] = (x + dx, y + dy, curr_cost, [mapper[curr_direction]])
                            heapq.heappush(q, bfs_map[x + dx][y + dy])
                        # elif prev_cost == curr_cost:
                        #     # print(f"(3) 기존 방향 {d}, 가려는 방향 {curr_direction} cost={curr_cost}")
                        #     bfs_map[x + dx][y + dy][3].append(mapper[curr_direction])
                        #     set(bfs_map[x + dx][y + dy][3])
                        #     heapq.heappush(q, bfs_map[x + dx][y + dy])
                            
    return bfs_map[len(board)-1][len(board)-1][2] * 100
