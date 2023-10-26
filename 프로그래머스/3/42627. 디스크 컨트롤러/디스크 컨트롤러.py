import heapq

def solution(jobs):
    answer = 0
    total_jobs = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)  # jobs.pop을 빠르게 하기 위해 시작 시간이 빠른 순서로 '내림차순' 정렬
    
    curr_time = jobs[-1][1] + jobs[-1][0]
    answer += jobs[-1][1]
    jobs.pop(-1)
    
    while jobs:
        min_heap = []
        # 1. curr_time 이전에 들어온 요청을 최소힙에 push
        for idx in range(len(jobs)-1, -1, -1):
            start, task = jobs[idx]
            if start <= curr_time:
                heapq.heappush(min_heap, (task, idx))
        
        if min_heap:
            task, idx = heapq.heappop(min_heap)
            answer += (curr_time + task - jobs[idx][0])
            curr_time += task
            jobs.pop(idx)
        else:
            # 2. 최소힙이 비어 있다면, curr_time 이후에 들어온 요청 중 맨 처음 요청을 처리
            answer += jobs[-1][1]
            curr_time = jobs[-1][0] + jobs[-1][1]
            jobs.pop(-1)
            
    return answer // total_jobs
