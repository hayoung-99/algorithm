def solution(storey):
    num = str(storey)
    answer = 0

    if 6 <= int(num[0]) <= 9:
        answer += 1
        num = str((10 ** len(num)) - storey)

    while int(num) > 0:
        # print(f"{num}, {answer}")
        if len(num) == 1:
            answer += int(num)
            break

        if 6 <= int(num[0]) <= 9:
            answer += 1
            num = str((10 ** len(num)) - int(num))

        else:
            if 0 <= int(num[1]) <= 5:
                answer += int(num[0])
                num = str(int(num) - (int(num[0]) * 10 ** (len(num) - 1)))

            else:
                answer += (int(num[0]) + 1)
                num = str((int(num[0]) + 1) * (10 ** (len(num) - 1)) - int(num))

    return answer