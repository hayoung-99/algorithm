def solution(weights):
    answer = 0
    overlap_dict = {}
    rates = [(3, 2), (4, 2), (4, 3)]  # 2:3, 2:4, 3:4

    # 1-1) 중복 개수 구하기
    for i in range(len(weights)):
        if weights[i] not in overlap_dict:
            overlap_dict[weights[i]] = 1
        else:
            overlap_dict[weights[i]] += 1

    # 1-2) 1:1 비율의 짝꿍 구하기
    for w in overlap_dict.values():
        if w >= 2:
            answer += int((w * (w - 1)) / 2)

    # 2) 1:1 비율 외의 다른 비율의 짝꿍 구하기
    for i in range(len(weights)):
        for rate in rates:
            target = weights[i] * rate[0] / rate[1]  # 짝꿍이 될 수 있는 몸무게
            if target in overlap_dict:  # 찾는 몸무게가 dict에 있다면 그 개수를 answer에 업데이트
                answer += overlap_dict[target]

    return answer

# 정리)
# "1:1 비율"은 따로 중복 수를 구한 dict를 이용해 n*(n-1)/2로 짝꿍 수를 구한다.
# "그 외 비율"은 weights 전체 for문 1번을 순회하여 자신과 짝꿍이 될 수 있는 몸무게를 구해서
# 앞서 구한 중복 수 dict에 해당 몸무게가 있으면 그 사람들의 수를 답에 갱신 