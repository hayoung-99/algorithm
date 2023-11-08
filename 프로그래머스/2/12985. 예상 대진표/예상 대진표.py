def swap(a, b):
    return b, a


def solution(n,a,b):
    if a > b:
        a, b = swap(a, b)
        
    curr_round = 1
    while True:
        # 현재 라운드에 만나는 경우
        if a % 2 == 1 and a + 1 == b:
            break
                
        # 다음 부여받을 번호 결정
        a = a // 2 if a % 2 == 0 else (a // 2) + 1
        b = b // 2 if b % 2 == 0 else (b // 2) + 1
            
        curr_round += 1
        
    return curr_round
                
        
                