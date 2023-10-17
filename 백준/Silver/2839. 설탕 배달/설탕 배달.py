n = int(input())

if n == 3 or n == 5:
    print(1)
else:
    memo = set([0])
    answer = 0
    while True:
        answer += 1
        temp = set()
        for s in memo:
            temp.add(s + 5)
            temp.add(s + 3)

        if n in temp:
            print(answer)
            break

        if min(list(temp)) > n:
            print(-1)
            break

        memo = temp

