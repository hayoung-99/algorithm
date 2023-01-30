def solution(weights):
    answer = 0
    for i in range(len(weights)):
        dic = {}
        for k in range(2, 5):
            dic[weights[i] * k] = True

        for j in range(i + 1, len(weights)):
            for w in range(2, 5):
                if (weights[j] * w) in dic:
                    answer += 1
                    break

    return answer