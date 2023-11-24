from collections import deque

def bfs(adj, dist):
    global max_dist
    
    q = deque()
    q.append((1, 0))
    
    while q:
        curr, curr_dist = q.popleft()
        for v in adj[curr]:
            if v != 1 and dist[v] == 0:
                dist[v] = curr_dist + 1
                max_dist = max(max_dist, dist[v])
                q.append((v, dist[v]))


def solution(n, edge):
    global max_dist
    max_dist = 0
    dist = [0 for _ in range(n + 1)]
    
    # 인접 리스트 만들기
    adj = [[] for _ in range(n + 1)]
    for s, e in edge:
        adj[s].append(e)
        adj[e].append(s)
        
    bfs(adj, dist)
    
    answer = 0
    for i in range(1, n + 1):
        if dist[i] == max_dist:
            answer += 1
            
    return answer