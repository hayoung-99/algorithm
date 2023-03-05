def solution(board, skill):
    r, c = len(board), len(board[0])
    buildings = r * c

    for sk in skill:
        r1, c1, r2, c2 = tuple(sk[1:-1])
        degree = sk[-1]
        # 1. 공격
        if sk[0] == 1:
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    board[x][y] -= degree
                    if board[x][y] + degree > 0 and board[x][y] <= 0:
                        buildings -= 1
        # 2. 회복
        elif sk[0] == 2:
            for x in range(r1, r2 + 1):
                for y in range(c1, c2 + 1):
                    board[x][y] += degree
                    if board[x][y] - degree <= 0 and board[x][y] > 0:
                        buildings += 1

    return buildings
