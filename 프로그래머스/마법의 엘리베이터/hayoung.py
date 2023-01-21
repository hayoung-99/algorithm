def solution(storey):
    num = str(storey)
    answer = 0

    while int(num) > 0:
        if len(num) == 1:
            answer += int(num)
            break

        if 0 <= int(num[1]) <= 5:
            answer += int(num[0])
            num = str(int(num) - (int(num[0]) * 10 ** (len(num) - 1)))

        else:
            answer += (int(num[0]) + 1)
            num = str((int(num[0]) + 1) * (10 ** (len(num) - 1)) - int(num))

    return answer
