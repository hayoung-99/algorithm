import heapq


def solution(n, k, enemy):
    k_list = enemy[:k]
    heapq.heapify(k_list)
    answer = 0

    for i in range(k, len(enemy)):
        print(k_list)
        if k_list[0] < enemy[i]:
            cur_k_min = heapq.heappop(k_list)
            heapq.heappush(k_list, enemy[i])

            n -= cur_k_min

        else:
            n -= enemy[i]

        if n < 0:
            answer = i
            break

    print(answer)

