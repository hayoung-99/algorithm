# 1. 구할 수 있는 영문쌍만 필터링 & 대문자 치환
# 2. set를 이용해 교집합 & 합집합 구하기
# 3. min, max 구해서 자카드 유사도 구하기
import re
import math
def solution(str1, str2):
    
    str1_set = [str1[i:i+2].upper() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]', str1[i:i+2])]
    str2_set = [str2[i:i+2].upper() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]', str2[i:i+2])]
    
    intersection = set(str1_set) & set(str2_set)
    union = set(str1_set) | set(str2_set)
    
    # 공집합인 경우
    if not union:
        return 65536
    
    jac_intersection = [min(str1_set.count(i), str2_set.count(i)) for i in intersection]
    jac_union = [max(str1_set.count(u), str2_set.count(u)) for u in union]
    
    return math.floor(sum(jac_intersection) / sum(jac_union) * 65536)
        