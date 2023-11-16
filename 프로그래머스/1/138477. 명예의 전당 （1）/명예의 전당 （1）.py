def solution(k, score):
    high_score_list = []
    result = []
    
    for s in score:
        # 우선 점수를 리스트에 push하고 정렬(klogk)
        high_score_list.append(s)
        high_score_list.sort(reverse=True)
        
        # 리스트가 k 크기보다 초과했으면 pop(정렬되어 있는 상태이므로 pop한 값은 최솟값)
        if len(high_score_list) > k:
            high_score_list.pop()
            
        # 현재 리스트에서 최솟값(가장 마지막에 있는 원소)을 answer에 적재
        result.append(high_score_list[-1])
    
    return result