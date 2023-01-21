def solution(storey):
    num = storey

    # 2번째 자릿수(i)부터 탐색해서
    # 1) num[i] = 0 ~ 5 => num[i] + 1
    # 2) num[i] = 6 ~ 9 => num[i]
    # 1)에 부합하면 num = (num[i] + 1) * 10^(자릿수) - num 으로 업데이트
    # 2)에 부합하면 num = num - (num[i] * 10^(자릿수))으로 업데이트
