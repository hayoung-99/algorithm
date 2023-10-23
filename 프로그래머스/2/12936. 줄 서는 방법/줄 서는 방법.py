def getFactorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
        
    return answer
    

def solution(n, k):
    answer = []
    candidates = [i+1 for i in range(n)]
    
    curr = k
    while curr > 0:
        if curr == 1:
            answer += candidates
            return answer
        
        fac = getFactorial(len(candidates) - 1)
        
        # 1. 나누어 떨어지는 경우
        if curr % fac == 0:
            answer.append(candidates[(curr // fac) - 1])
            candidates.pop((curr // fac) - 1)
            answer += candidates[::-1]
            return answer
        
        else:
            mock = curr // fac
            rest = curr % fac
            answer.append(candidates[mock])
            candidates.pop(mock)
            curr = rest
    
    return answer

