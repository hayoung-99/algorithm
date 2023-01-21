def solution(storey):
    num = str(storey)
    answer = 0

    while int(num) > 0:
        if len(num) == 1:
            if 5 < int(num):
                answer += 1
                answer += (10 - int(num))
            else:
                answer += int(num)
            break

        target = int(num[0])
        if 5 <= int(num[1]):
            target += 1

        if 5 < target:
            answer += 1
            num = str(10 ** len(num) - int(num))

        else:
            answer += int(num[0])
            num = str(int(num) - int(num[0]) * (10 ** (len(num) - 1)))

    print(answer)
    return answer