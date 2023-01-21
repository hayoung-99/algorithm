def solution(storey):
    def calculate(acc, storey):
        r = storey % 10
        storey = int((storey - r) / 10)
        next_r = storey % 10
        if r > 5 or (next_r >= 5 and r >= 5):
            r = 10 - r
            storey += 1
        acc += r
        if storey < 10:
            if storey > 5:
                return acc + 1 + 10 - storey
            return acc + storey
        return calculate(acc, storey)

    answer = calculate(0, storey)
    return answer
