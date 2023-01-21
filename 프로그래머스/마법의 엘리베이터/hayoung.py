def solution(storey):
    num = str(storey)
    answer = 0

    while int(num) > 0:
        if 5 < int(num[0]):
            answer += 1
            num = str(10 ** len(num) - int(num))

        else:
            answer += int(num[0])
            num = str(int(num) - int(num[0]) * (10 ** (len(num) - 1)))

    print(answer)
    return answer