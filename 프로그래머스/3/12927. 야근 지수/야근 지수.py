def solution(n, works):
    # no 야근
    total_works = sum(works)
    if total_works <= n:
        return 0
    
    dic = {}
    curr_n = n
    curr_max = 0
    for work in works:
        curr_max = max(curr_max, work)
        if not work in dic:
            dic[work] = 1
        else:
            dic[work] += 1
            
    while curr_n > 0:
        if dic[curr_max] >= curr_n:
            dic[curr_max] -= curr_n
            if (curr_max - 1) in dic:
                dic[curr_max - 1] += curr_n
            else:
                dic[curr_max - 1] = curr_n
            break
        else:
            if (curr_max - 1) in dic:
                dic[curr_max - 1] += dic[curr_max]
            else:
                dic[curr_max - 1] = dic[curr_max]
            curr_n -= dic[curr_max]
            dic[curr_max] = 0
            curr_max -= 1
            
    answer = 0
    for k, v in dic.items():
        if v != 0:
            answer += (k * k) * v
            
    return answer
    