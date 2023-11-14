def solution(msg):
    answer = []
    
    # 사전 초기화
    dt = {}
    for i in range(ord('A'), ord('Z') + 1):
        dt[chr(i)] = i - ord('A') + 1
        
    idx_num = 27  # 색인 번호
    for i in range(0, len(msg)):
        if i == 0:
            curr = msg[0]
            continue
            
        next_msg = curr + msg[i]
        if next_msg in dt:
            curr = next_msg
            
        else:
            answer.append(dt[curr])
            dt[next_msg] = idx_num
            idx_num += 1
            curr = msg[i]

    # 마지막으로 처리되지 않은 글자 처리
    answer.append(dt[curr])

    return answer