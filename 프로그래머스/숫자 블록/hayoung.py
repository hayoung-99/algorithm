def max_factor(n):
    import math

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factor = int(n / i)
            return factor

    return 0


def solution(begin, end):
    li = [1 for _ in range(end - begin + 1)]
    if begin == 1:
        li[0] = 0

    for i in range(begin, end + 1):
        # 현재 (인덱스+1)이...
        # 1) 소수라면 1 (<- 리스트 초기화를 1로 했으므로 따로 작업 x)
        # 2) 소수가 아니라면 자기 자신을 제외한 가장 큰 인수를 저장
        factor = max_factor(i)
        if factor:
            li[i - begin] = factor

    return li