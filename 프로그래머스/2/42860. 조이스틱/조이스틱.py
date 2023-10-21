def getMinMoves(char):
    alphabets = ord('Z') - ord('A') + 1
    return min(ord(char) - ord('A'), ord('A') + alphabets - ord(char))


def solution(name):
    answer = 20  # 최대 좌우 이동 횟수
    
    # 1. 좌우 이동 횟수
    # 오른쪽으로 끝까지 진행
    for i in range(len(name) - 1, -1, -1):
        if name[i] != 'A':
            answer = min(answer, i)
            break
            
    # 왼쪽으로 끝까지 진행
    for i in range(-len(name) + 1, 0):
        if name[i] != 'A':
            answer = min(answer, abs(i))
            break

    for i in range(len(name)):
        # 오른쪽으로 진행하다가 왼쪽으로 터닝
        for k in range(i+1, len(name)):
            if name[k] != 'A':
                answer = min(answer, len(name) - k + (2 * i))
                break
        
        # 왼쪽으로 진행하다가 오른쪽으로 터닝
        for k in range(len(name) - i - 1, 0, -1):
            if name[k] != 'A':
                answer = min(answer, (2 * i) + k)
                break
                
    # 예외) 모든 문자가 'A'인 경우
    if 'A' * len(name) == name:
        answer = 0
        
    # 2. 상하 이동 횟수
    for ch in name:
        answer += getMinMoves(ch)
    
    return answer