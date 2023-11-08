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

    # 1. 후보 목록 생성
    for combi in combinations(user_id, len(banned_id)):
        # 2. 후보 목록의 '순서'에 맞게 banned_id 목록 생성
        for perm in permutations(banned_id, len(banned_id)):
            matches = 0
            # 3. 후보 목록과 banned_id가 일치하면 다음 후보 목록 탐색
            for target, curr_banned_id in zip(combi, perm):
                if match(target, curr_banned_id):
                    matches += 1
                else:
                    break

            if matches == len(banned_id):
                answer += 1
                break

    return answer