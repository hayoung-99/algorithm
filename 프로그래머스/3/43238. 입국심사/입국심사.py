def solution(n, times): 
    answer = 0
    s, e = 0, min(times) * n
    
    # 이분탐색으로 최소한으로 걸리는 시간을 탐색해나간다.
    while s <= e:
        m = (s + e) // 2
        
        curr_n = 0
        for t in times:
            curr_n += m // t
            
            if curr_n >= n:
                break
                
        if curr_n >= n:
            answer = m
            e = m - 1
        else:
            s = m + 1
            
    return answer