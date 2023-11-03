def solution(msg):
    answer = []
    
    # 사전 초기화
    dt = {}
    for i in range(ord('A'), ord('Z') + 1):
        dt[chr(i)] = i - ord('A') + 1
        
    curr = msg[0]
    idx = 1
    add_num = 27
    while idx < len(msg):
        if curr in dt:
            curr += msg[idx]
            idx += 1
            
        else:
            answer.append(dt[curr[:-1]])
            dt[curr] = add_num
            add_num += 1
            curr = curr[-1]

    # 마지막으로 처리되지 않은 글자 처리
    if curr not in dt:
        answer.append(dt[curr[:-1]])
        curr = curr[-1]
    answer.append(dt[curr])

    return answer