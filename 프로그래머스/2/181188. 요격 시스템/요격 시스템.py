def solution(targets):
    # 끝 지점을 기준으로 오름차순 정렬
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    shoot = -1
    for target in targets:
        s, e = target
        if s > shoot:
            answer += 1
            shoot = e - 0.5
            
    return answer
        