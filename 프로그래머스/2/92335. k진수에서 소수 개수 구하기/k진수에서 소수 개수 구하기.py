import math

def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

def solution(n, k):
    # k진법 변환 및 변환 결과를 str로 변환
    if k < 10:
        temp = ""
        while n >= k:
            r = n % k
            temp = str(r) + temp
            n //= k
        temp = str(n) + temp
        n = temp
    else:
        n = str(n)
        
    candidates = n.split("0")
    
    answer = 0
    for c in candidates:
        if c == "1" or c == "":
            continue
            
        if isPrime(int(c)):
            answer += 1
            
    return answer