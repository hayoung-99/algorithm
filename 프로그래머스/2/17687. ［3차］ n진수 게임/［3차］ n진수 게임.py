def convert(n, k, dt):
    if n == 0:
        return '0'
    
    curr = ""
    while n:
        if n % k >= 10:
            curr += dt[n % k]
        else:
            curr += str(n % k)
        n //= k
        
    return curr[::-1]

            
def solution(n, t, m, p):
    
    dt = {
        10: 'A',
        11: 'B', 
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    
    answer = ''
    curr = ''
    num = 0
    while len(curr) < t * m:
        curr += convert(num, n, dt)
        num += 1
        
    idx = p - 1
    while len(answer) < t:
        answer += curr[idx]
        idx += m
    
    return answer
