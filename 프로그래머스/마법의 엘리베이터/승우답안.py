from math import log10, floor, pow


def solution(storey):
    def calculate(acc, storey):
        log_storey = log10(storey)
        a = floor(log_storey)
        A = pow(10, a)
        b = floor(storey / A)
        B = int(b * A)
        r = storey - B
        if b > 5:
            b = 10 - b
            acc += 1
        acc += b
        if not r:
            return acc
        else:
            return calculate(acc, r)

    answer = calculate(0, storey)
    return answer


print(solution(16))
