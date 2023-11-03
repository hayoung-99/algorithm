import math

def convertToK(n, k):
    if k < 10:
        temp = ""
        while n:
            temp = str(n % k) + temp
            n //= k
        return temp
    return str(n)


def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

def solution(n, k):
    # k진법 변환 및 변환 결과를 str로 변환
    n = convertToK(n, k)
    
    answer = 0
    for c in n.split("0"):
        if c == "1" or c == "":
            continue
            
        if isPrime(int(c)):
            answer += 1
            
    return answer