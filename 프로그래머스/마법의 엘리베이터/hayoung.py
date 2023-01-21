def solution(storey):
    num = str(storey)
    answer = 0

    while True:
        if len(num) == 1:
            if int(num) <= 5:
                answer += int(num)
            else:
                answer += 1
                answer += (10 - int(num))
            break

        if 6 <= int(num[0]):
            answer += 1
            num = str((10 ** len(num)) - int(num))

        else:
            if int(num[1]) <= 5:
                answer += int(num[0])
                num = str(int(num) - (int(num[0]) * 10 ** (len(num) - 1)))

            else:
                answer += (int(num[0]) + 1)
                num = str((int(num[0]) + 1) * (10 ** (len(num) - 1)) - int(num))

    return answer