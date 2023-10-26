import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    jobs.sort()  # 시작 시간이 빠른 순서대로 오름차순 정렬
    
    curr_time = jobs[0][1] + jobs[0][0]
    answer += jobs[0][1]
    jobs.pop(0)
    
    while jobs:
        min_heap = []
        for i in range(len(jobs)):
            task = jobs[i][1]
            heapq.heappush(min_heap, (task, i))
                
        late_task = True
        task, idx = 0, 0
        while min_heap:
            t, i = heapq.heappop(min_heap)
            if jobs[i][0] >= curr_time:
                if task == 0 or jobs[i][0] < jobs[idx][0]:
                    task, idx = t, i
                
            else:
                answer += t + curr_time - jobs[i][0]
                curr_time += t
                jobs.pop(i)
                late_task = False
                break
                
        if late_task:
            answer += task
            curr_time = task + jobs[idx][0]
            jobs.pop(idx)
            
    return answer // length
