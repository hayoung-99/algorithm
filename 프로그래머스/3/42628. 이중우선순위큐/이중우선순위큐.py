# 두 힙의 동기화를 맞추는 것이 포인트
# 1. 한 쪽의 힙이 비어 있다면 다른 힙도 비어 있어야 된다.
# 2. 최대힙의 최댓값과 최소힙의 최솟값 중, 최댓값이 더 작을 경우 두 힙의 상황이 반전되었으므로 이는 곧 힙이 비었음을 의미

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        option, number = op.split()
        number = int(number)
        
        if option == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            
        elif option == "D":
            if number == 1:
                if max_heap:
                    heapq.heappop(max_heap)
                    if not max_heap or -max_heap[0] < min_heap[0]:
                        min_heap = []
                        max_heap = []
                        
            else:
                if min_heap:
                    heapq.heappop(min_heap)
                    if not min_heap or -min_heap[0] < max_heap[0]:
                        min_heap = []
                        max_heap = []
                        
    answer = [0, 0]
    if max_heap:  # 한 쪽의 힙이 존재한다면 다른 힙도 존재한다.
        answer[0] = -max_heap[0]
        answer[1] = min_heap[0]
        
    return answer
