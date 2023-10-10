from itertools import combinations

def solution(clothes):
    answer = 1
    
    # 종류별 의상 개수 구하기
    closet = {} 
    
    for _, category in clothes:
        if category not in closet:
            closet[category] = 1
        else:
            closet[category] += 1
            
    # 수학적 접근) 각 종류의 옷을 최대 1개를 입는다고 했을 때, 
    # 입을 수 있는 모든 옷의 종류 = (A+1) * (B+1) * (C+1) .. - 1
    # => 옷을 하나도 안 입는 경우인 1을 빼준다.
    for l in list(closet.values()):
        answer = answer * (l + 1)
    
    return answer - 1