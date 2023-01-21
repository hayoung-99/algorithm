def solution(storey):
    def calculate(acc, storey):
        r = storey % 10
        if r > 5:
            r = 10 - r
            storey += 10 - r
        acc += r
        storey = int(storey / 10)
        if storey < 10:
            if storey > 5:
                return acc + 1 + 10 - storey
            return acc + storey
        return calculate(acc, storey)

    answer = calculate(0, storey)
    return answer
