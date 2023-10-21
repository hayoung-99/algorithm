def solution(n):
    pos = [[0 for _ in range(i)] for i in range(1, n+1)]

    end = n * (n + 1) // 2
    
    num = 1
    curr_col = 0
    steps = n
    direction = 0  # 0: down, 1: right, 2: up
    while num <= end:
        if direction == 0:
            for _ in range(steps):
                curr_col += 1
                for i in range(curr_col):
                    if pos[curr_col - 1][i] == 0:
                        pos[curr_col - 1][i] = num
                        num += 1
                        break
        elif direction == 1:
            for i in range(curr_col):
                if pos[curr_col - 1][i] == 0:
                    pos[curr_col - 1][i] = num
                    num += 1
        else:
            for _ in range(steps):
                curr_col -= 1
                for i in range(curr_col - 1, -1, -1):
                    if pos[curr_col - 1][i] == 0:
                        pos[curr_col - 1][i] = num
                        num += 1
                        break
        
        steps -= 1
        direction = (direction + 1) % 3
        
    answer = []
    for i in pos:
        for k in i:
            answer.append(k)
            
    return answer