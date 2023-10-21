def solution(n):
    end = (n * (n + 1)) // 2
    answer = [0 for _ in range(end)]
    
    direction = 0  # 0: down, 1: right, 2: up
    curr_col = 0
    idx = 0
    steps = n
    num = 1
    
    while num <= end:
        # 1. 행 칸만큼 앞으로 이동
        if direction == 0:
            for _ in range(steps):
                idx += curr_col
                answer[idx] = num
                curr_col += 1
                num += 1
            
        elif direction == 1:
            for _ in range(steps):
                idx += 1
                answer[idx] = num
                num += 1
                
        # 2. 현재 idx에서 steps만큼 진행
        else:
            for _ in range(steps):
                idx -= curr_col
                answer[idx] = num
                curr_col -= 1
                num += 1
                
        # 3. 행 칸만큼 뒤로 이동
        direction = (direction + 1) % 3
        steps -= 1

    return answer