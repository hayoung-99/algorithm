def max_factor(n):
    import math

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            max_factor = int(n / i)
            # 포인트) 도로 길이는 최대 10억이지만 블록 수가 "최대 1천만"이므로, 1천만을 넘지 않는 최대 약수를 구한다.
            if max_factor <= 10000000:
                return max_factor

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