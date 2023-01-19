# 최소힙 사용
# enemy 배열 처음부터 k개는 무적권을 사용한다고 가정하고, 무적권을 사용할 적의 수를 최소힙에 저장(k_list)
# k_list[0]는 최소힙의 최솟값으로, (k+1)번째 적부터 현재 적의 수(enemy[i])와 k_list[0]의 값을 비교하여,
#   1) k_list[0]가 더 작을 경우: 현재 적의 수(enemy[i])는 최소힙에 push, 현재 남아 있는 병사 n에서 k_list[0]를 뺀다.
#   2) 반대로 k_list[0] >= enemy[i]: 현재 남아 있는 병사 n - enemy[i]
# 예외 사항 1) n이 충분히 커서 모든 enemy[i]를 방어하고도 남는 경우: answer = enemy 길이
# 예외 사항 2) k >= enemy 길이: answer = enemy 길이

# 시간 복잡도
# 최소힙 생성 = O(klogk)
# 최소힙 삭제 & 재구조화 = O(logk)
# 전체 프로그램: enemy 전체 1번 순회 = "O(n)"

import heapq


def solution(n, k, enemy):
    k_list = enemy[:k]
    heapq.heapify(k_list)
    answer = 0

    if k >= len(enemy):
        return len(enemy)

    for i in range(k, len(enemy)):
        if k_list[0] < enemy[i]:
            cur_k_min = heapq.heappop(k_list)
            heapq.heappush(k_list, enemy[i])

            n -= cur_k_min

        else:
            n -= enemy[i]

        if n < 0:
            answer = i
            break

        if i == (len(enemy) - 1):
            if n >= 0:
                answer = len(enemy)

    return answer

