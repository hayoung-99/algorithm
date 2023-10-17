# roo1과 연결돼있으면서, root2와 연결되지 않은 전력망 수
def dfs(root1, root2, inj, curr, visited): 
    for w in inj[curr]:
        if not visited[w] and w != root2:
            visited[w] = 1
            dfs(root1, root2, inj, w, visited)
    

def solution(n, wires):
    answer = 100
    
    # 인접리스트 생성
    inj = [[] for _ in range(n + 1)]  # 인덱스 0은 쓰지 않는다
    
    for w1, w2 in wires:
        inj[w1].append(w2)
        inj[w2].append(w1)
    
    for root1, root2 in wires:
        visited = [0] * (n+1)  # 인덱스 0은 쓰지 않는다.
        
        # root1의 전력망 개수
        visited[root1] = 1  # root1부터 방문해서 근접한 전력망을 찾는다.
        dfs(root1, root2, inj, root1, visited)
        
        sum1 = 0
        for v in visited:
            if v == 1:
                sum1 += 1
        
        sum2 = n - sum1
        
        if answer > abs(sum1 - sum2):
            answer = abs(sum1 - sum2)
            
    return answer
            