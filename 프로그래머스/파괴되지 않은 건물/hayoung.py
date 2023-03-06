def solution(board, skill):
    w, h = len(board[0]), len(board)
    buildings = w * h
    temp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for sk in skill:
        r1, c1, r2, c2 = tuple(sk[1:-1])
        degree = sk[-1]
        # 누적합 표시 작업
        # step 1. 공격 or 회복 시작 지점에 degree 표시
        # step 2. 공격 or 회복 시작 행에서 마지막 지점의 뒤에 있는 지점(r1, c2+1)에 degree 표시
        # step 3. 공격 or 회복 시작 열에서 마지막 지점의 뒤에 있는 지점(r2+1, c1)에 degree 표시
        # step 4. 공격 or 회복 마지막 지점의 뒤에 있는 지점(r2+1, c2+1)에 degree 표시

        # 공격
        if sk[0] == 1:
            temp[r1][c1] -= degree
            temp[r1][c2 + 1] += degree
            temp[r2 + 1][c1] += degree
            temp[r2 + 1][c2 + 1] -= degree

        # 회복
        elif sk[0] == 2:
            temp[r1][c1] += degree
            temp[r1][c2 + 1] -= degree
            temp[r2 + 1][c1] -= degree
            temp[r2 + 1][c2 + 1] += degree

    total_sum_map = [[0 for _ in range(w)] for _ in range(h)]

    # 현 지점 누적합 = 현 지점 위의 누적합 + 현 지점까지의 행 누적합
    for x in range(h):
        curr = 0
        for y in range(w):
            curr += temp[x][y]
            # 첫 행은 위의 누적합이 없으므로 현 지점의 행 누적합 = 현 지점 누적합
            if x == 0:
                total_sum_map[x][y] = curr
            else:
                total_sum_map[x][y] = total_sum_map[x - 1][y] + curr

            if board[x][y] + total_sum_map[x][y] <= 0:
                buildings -= 1

    return buildings
