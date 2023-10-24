# 1. 모든 곡괭이 수를 구한다.
# 2. 곡괭이 수 만큼 캘 수 있는 minerals를 쪼갠다.
# 3. minerals를 5개씩 쪼갠 뒤, 다이아몬드, 철, 돌 개수별로 구한다.
# 4. 다이아몬트 > 철 > 돌 순으로 내림차순 정렬한다.
# 5. 정렬된 minerals를 이용해 다이아몬트 > 철 > 돌 곡괭이 순으로 캐나간다. 

def solution(picks, minerals):
    mapper = {
        "diamond": 0,
        "iron": 1,
        "stone": 2,
    }
    costs = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]
    
    # 1
    total_picks = 0
    for pick in picks:
        total_picks += pick
        
    minerals = minerals[:total_picks * 5]  # 2
    minerals_per_five = []
    idx = 0
    
    # 3
    while idx < len(minerals):
        curr_target = [0, 0, 0]
        curr_minerals = minerals[idx:idx+5]
        for cm in curr_minerals:
            curr_target[mapper[cm]] += 1
        minerals_per_five.append(curr_target)
        idx += 5
        
    # 4
    minerals_per_five.sort(reverse=True)
    
    # 5
    curr_pick = 0
    answer = 0
    for minerals in minerals_per_five:
        for p in range(len(picks)):
            if picks[p] != 0:
                curr_pick = p
                break
                
        for i in range(3):
            answer += minerals[i] * costs[curr_pick][i]
            
        picks[curr_pick] -= 1

    return answer