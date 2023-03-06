def solution(board, skill):
    h, w = len(board), len(board[0])
    buildings = h * w

    total_sum_map = [[0 for _ in range(w + 1)] for _ in range(h)]

    for sk in skill:
        r1, c1, r2, c2 = tuple(sk[1:-1])
        degree = sk[-1]
        # 1. 공격
        if sk[0] == 1:
            for x in range(r1, r2 + 1):
                total_sum_map[x][c1] -= degree
                total_sum_map[x][c2 + 1] += degree

        # 2. 회복
        elif sk[0] == 2:
            for x in range(r1, r2 + 1):
                total_sum_map[x][c1] += degree
                total_sum_map[x][c2 + 1] -= degree

    for x in range(h):
        curr_total = 0
        for y in range(w):
            curr_total += total_sum_map[x][y]
            if board[x][y] + curr_total <= 0:
                buildings -= 1

    return buildings
