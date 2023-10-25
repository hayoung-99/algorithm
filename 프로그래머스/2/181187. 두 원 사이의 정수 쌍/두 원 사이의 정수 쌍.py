import math

def maxNumber(n):
    answer = int(math.sqrt(n))
    return answer
        
        
def maxNumber2(n):
    answer = int(math.sqrt(n))
    if answer * answer == n:
        return answer - 1
    return answer


def solution(r1, r2):
    # r2 내의 정수 쌍 구하기
    r2_answer = 0
    for x in range(1, r2):
        yRange = maxNumber(r2 * r2 - x * x)
        r2_answer += yRange
        
    # r1 내의 정수 쌍 구하기
    r1_answer = 0
    for x in range(1, r1):
        yRange = maxNumber2(r1 * r1 - x * x)
        r1_answer += yRange
            
    # print(r2_answer, r1_answer)
            
    # 4분면
    answer = (r2_answer - r1_answer) * 4
    
    # x축, y축 위의 정수 쌍 구하기
    answer += (r2 + 1 - r1) * 4
    
    return answer
        
    
        