def getFactorial(n):  # n!
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer


def solution(n, k):
    answer = []
    numList = [i+1 for i in range(n)]
    
    curr = k - 1
    while curr >= 1:
        fac = getFactorial(len(numList) - 1)
        idx = curr // fac
        answer.append(numList[idx])
        numList.pop(idx)
        
        curr = curr % fac
        
    # 아직 넣지 않은 숫자가 있을 경우 그대로 이어 붙인다.
    answer += numList
    
    return answer