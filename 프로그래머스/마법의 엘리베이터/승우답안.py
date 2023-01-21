from math import fmod


def solution(storey):
    def calculate(acc, storey):
        r = int(fmod(storey, 10))
        if r > 5:
            r = 10 - r
            storey += 10
        acc += r
        storey = int(storey / 10)
        if storey < 10:
            if storey > 5:
                return acc + 1 + 10 - storey
            return acc + storey
        return calculate(acc, storey)

    answer = calculate(0, storey)
    return answer


print(solution(2554))
print(solution(16))
