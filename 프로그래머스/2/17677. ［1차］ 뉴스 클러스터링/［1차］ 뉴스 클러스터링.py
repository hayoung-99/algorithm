# 1. 알파벳을 모두 대문자로 치환한 뒤, 구할 수 있는 영문쌍만 필터링
# 2. dict로 mix, max 구해서 자카드 유사도 구하기
def getJaccardSimilarity(str1, str2):
    str1_dict = {}
    str2_dict = {}
    
    for s1 in str1:
        if s1 not in str1_dict:
            str1_dict[s1] = 1
        else:
            str1_dict[s1] += 1
    
    for s2 in str2:
        if s2 not in str2_dict:
            str2_dict[s2] = 1
        else:
            str2_dict[s2] += 1
            
    # 교집합
    answer1 = 0
    intersection = set(str1) & set(str2)
    for i in intersection:
        answer1 += min(str1_dict[i], str2_dict[i])
    
    # 합집합
    answer2 = 0
    union = set(str1) | set(str2)
    for u in union:
        # 1. set1에만 있는 경우
        if u in str1_dict and u not in str2_dict:
            answer2 += str1_dict[u]
            continue
        # 2. str2_dict에만 있는 경우
        if u in str2_dict and u not in str1_dict:
            answer2 += str2_dict[u]
            continue
        # 3. str1_dict, str2_dict 모두에 있는 경우 
        answer2 += max(str1_dict[u], str2_dict[u])
        
    if answer2 == 0:
        return 1
    return answer1 / answer2


def solution(str1, str2):
    import math
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    str1_set = []
    str2_set = []
    
    for i in range(len(str1)-1):
        curr = str1[i:i+2]
        if 'A' <= curr[0] <= 'Z' and 'A' <= curr[1] <= 'Z':
            str1_set.append(curr)
    for i in range(len(str2)-1):
        curr = str2[i:i+2]
        if 'A' <= curr[0] <= 'Z' and 'A' <= curr[1] <= 'Z':
            str2_set.append(curr)
            
    answer = getJaccardSimilarity(str1_set, str2_set)
    return math.floor(answer * 65536)
        