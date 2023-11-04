# # roo1과 연결돼있으면서, root2와 연결되지 않은 전력망 수
# def dfs(root1, root2, inj, curr, visited): 
#     for w in inj[curr]:
#         if not visited[w] and w != root2:
#             visited[w] = 1
#             dfs(root1, root2, inj, w, visited)
    

# def solution(n, wires):
#     answer = 100
    
#     # 인접리스트 생성
#     inj = [[] for _ in range(n + 1)]  # 인덱스 0은 쓰지 않는다
    
#     for w1, w2 in wires:
#         inj[w1].append(w2)
#         inj[w2].append(w1)
    
#     for root1, root2 in wires:
#         visited = [0] * (n+1)  # 인덱스 0은 쓰지 않는다.
        
#         # root1의 전력망 개수
#         visited[root1] = 1  # root1부터 방문해서 근접한 전력망을 찾는다.
#         dfs(root1, root2, inj, root1, visited)
        
#         sum1 = 0
#         for v in visited:
#             if v == 1:
#                 sum1 += 1
        
#         sum2 = n - sum1
        
#         if answer > abs(sum1 - sum2):
#             answer = abs(sum1 - sum2)
            
#     return answer
            
    

# def solution(n, wires):
#     ans = n
#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
#         print(sub)
#         s = set(sub[0])
#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         ans = min(ans, abs(2 * len(s) - n))
#     return ans

def connected(inj, n, k, visited):
    for i in inj[n]:
        if not visited[i] and i != k:
            visited[i] = 1
            connected(inj, i, k, visited)
        

def solution(n, wires):
    # 인접 리스트
    inj = [[] for _ in range(n+1)]
    for s, e in wires:
        inj[s].append(e)
        inj[e].append(s)
        
    answer = 100
    for s, e in wires:
        # s와 연결된 송전탑 개수
        visited = [0 for _ in range(n+1)]
        visited[s] = 1
        s_num = 0
        connected(inj, s, e, visited)
        
        cnt = visited.count(1)
        n1, n2 = cnt, n - cnt
        
        answer = min(answer, abs(n1 - n2))
        
    return answer
        