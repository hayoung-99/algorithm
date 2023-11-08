from itertools import combinations, permutations

def match(a, b):
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if b[i] != '*' and a[i] != b[i]:
            return False
        
    return True
    

def solution(user_id, banned_id):
    answer = 0
    
    for combi in combinations(user_id, len(banned_id)):
        for perm in permutations(banned_id, len(banned_id)):
            matches = 0
            for target, curr_banned_id in zip(combi, perm):
                if match(target, curr_banned_id):
                    matches += 1
                else:
                    break
                    
            if matches == len(banned_id):
                answer += 1
                break
    
    return answer