import heapq

def deleteMaxHeapItem(q1, q1_dict, q2_dict):
    while q1:
        _, num = q1[0]
        if num not in q1_dict:
            if num in q2_dict:
                q1_dict[num] = 1
                heapq.heappop(q1)
                continue
        elif num in q2_dict:
            if q1_dict[num] < q2_dict[num]:
                q1_delete_dict[num] += 1
                heapq.heappop(q1)
                continue
        break

        
def deleteMinHeapItem(q1, q1_dict, q2_dict):
    while q1:
        num = q1[0]
        if num not in q1_dict:
            if num in q2_dict:
                q1_dict[num] = 1
                heapq.heappop(q1)
                continue
        elif num in q2_dict:
            if q1_dict[num] < q2_dict[num]:
                q1_delete_dict[num] += 1
                heapq.heappop(q1)
                continue
        break
        
        
def solution(operations):
    min_heap = []
    max_heap = []
    min_heap_delete_dict = {}
    max_heap_delete_dict = {}
    
    for op in operations:
        option, number = op.split()
        
        # insert
        if option == "I":
            number = int(number)
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, (-number, number))
            
        # delete
        elif option == "D":
            # delete from max heap
            if number == "1":
                deleteMaxHeapItem(max_heap, max_heap_delete_dict, min_heap_delete_dict)
                    
                if max_heap:
                    _, num = heapq.heappop(max_heap)
                    if num not in max_heap_delete_dict:
                        max_heap_delete_dict[num] = 1 
                    else:
                        max_heap_delete_dict[num] += 1  
                
            # delete from min heap
            else:
                deleteMinHeapItem(min_heap, min_heap_delete_dict, max_heap_delete_dict)
                if min_heap:
                    num = heapq.heappop(min_heap)
                    if num not in min_heap_delete_dict:
                        min_heap_delete_dict[num] = 1 
                    else:
                        min_heap_delete_dict[num] += 1
    
    deleteMaxHeapItem(max_heap, max_heap_delete_dict, min_heap_delete_dict)
    deleteMinHeapItem(min_heap, min_heap_delete_dict, max_heap_delete_dict)
    answer = [0, 0]
    
    if max_heap:
        answer[0] = heapq.heappop(max_heap)[1]
    if min_heap:
        answer[1] = heapq.heappop(min_heap)
        
    return answer