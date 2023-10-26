import heapq

def solution(jobs):
    answer = 0
    total_jobs = len(jobs)
    jobs.sort()  # 시작 시간이 빠른 순서대로 정렬
    
    curr_time = jobs[0][1] + jobs[0][0]
    answer += jobs[0][1]
    jobs.pop(0)
    
    while jobs:
        min_heap = []
        # 1. curr_time 이전에 들어온 요청을 최소힙에 push
        for idx, job in enumerate(jobs):
            start, task = job
            if start <= curr_time:
                heapq.heappush(min_heap, (task, idx))
        
        if min_heap:
            task, idx = heapq.heappop(min_heap)
            answer += (curr_time + task - jobs[idx][0])
            curr_time += task
            jobs.pop(idx)
        else:
            # 2. 최소힙이 비어 있다면, curr_time 이후에 들어온 요청 중 맨 처음 요청을 처리
            answer += jobs[0][1]
            curr_time = jobs[0][0] + jobs[0][1]
            jobs.pop(0)
            
    return answer // total_jobs
