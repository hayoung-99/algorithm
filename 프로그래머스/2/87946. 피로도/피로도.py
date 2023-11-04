# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
    
#     for pmt in permutations(dungeons, len(dungeons)):
#         # 완전 탐색
#         p = k
#         temp = 0
#         for need_p, use_p in pmt:
#             if p >= need_p:
#                 temp += 1
#                 p -= use_p
#             else:
#                 break
#         answer = max(answer, temp)
                
#     return answer

from itertools import permutations

def solution(k, dungeons):
    p = list(permutations(dungeons, len(dungeons)))
    
    answer = 0
    for pp in p:
        kk = k
        temp = 0
        for need, reduce in pp:
            if kk >= need:
                temp += 1
                kk -= reduce
        answer = max(answer, temp)
        
    return answer