# from itertools import permutations

def permutations(arr, n):
    result = []
    
    if n == 1:
        for i in arr:
            result.append([i])
        return result
    
    if n > 1:
        for i in range(len(arr)):
            curr = [i for i in arr]
            curr.remove(curr[i])
            for p in permutations(curr, n-1):
                result.append([arr[i]] + p)
            
    return result
    

def solution(k, dungeons):
    answer = 0
    
    for pmt in permutations(dungeons, len(dungeons)):
        # 완전 탐색
        p = k
        temp = 0
        for need_p, use_p in pmt:
            if p >= need_p:
                temp += 1
                p -= use_p
            else:
                break
        answer = max(answer, temp)
        
    return answer