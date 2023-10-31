def solution(n, times): 
    answer = 0
    s, e = 0, times[0] * n
    
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