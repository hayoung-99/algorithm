from collections import deque

def solution(n, roads, sources, destination):
    # 인접 리스트 만들기
    inj = [[] for _ in range(n+1)]
    for s, e in roads:
        inj[s].append(e)
        inj[e].append(s)
    
    # BFS
    q = deque()
    q.append((destination, 0))
    distances = [-1 for _ in range(n+1)]
    distances[destination] = 0
    while q:
        curr, dist = q.popleft()
        for num in inj[curr]:
            if distances[num] == -1:
                distances[num] = dist + 1
                q.append((num, dist+1))
                
    answer = []
    for source in sources:
        answer.append(distances[source])
    return answer