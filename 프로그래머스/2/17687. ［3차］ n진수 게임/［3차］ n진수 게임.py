def convert(n, k, dt):
    if n == 0:
        return '0'
    
    curr = ""
    while n:
        curr += dt[n % k]
        n //= k
        
    return curr[::-1]

            
def solution(n, t, m, p):
    DIGITS = '0123456789ABCDEF'
    
    answer = ''
    curr = ''
    num = 0
    while len(curr) < t * m:
        curr += convert(num, n, DIGITS)
        num += 1
        
    idx = p - 1
    while len(answer) < t:
        answer += curr[idx]
        idx += m
    
    return answer
