def getLengthByBSearch(weights, idx, rate):
    length = 0
    target = weights[idx] * rate[0] / rate[1]
    # print(f"현재 idx={idx}, target={target}")
    left = idx + 1
    right = len(weights) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if weights[mid] == target:
            # 해당 target(중복) 개수 구하기
            for l in range(mid, idx, -1):  # 왼쪽
                if weights[l] == target:
                    length += 1
                else:
                    break
            for r in range(mid + 1, len(weights)):  # 오른쪽
                if weights[r] == target:
                    length += 1
                else:
                    break
            # print(f"{target} 발견: 개수 ({length})개")
            return length

        elif weights[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return length  # return 0


def solution(weights):
    answer = 0
    rates = [(1, 1), (3, 2), (4, 2), (4, 3)]  # 1:1, 2:3, 2:4, 3:4

    weights.sort()

    for i in range(len(weights)):
        # 이진 탐색으로 쌍 구하기
        for rate in rates:
            answer += getLengthByBSearch(weights, i, rate)

    return answer