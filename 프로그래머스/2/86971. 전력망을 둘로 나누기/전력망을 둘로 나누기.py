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
        
        # e와 연결된 송전탑 개수는, s와 연결된 송전탑 개수의 나머지로 바로 구할 수 있다.
        cnt = visited.count(1)
        n1, n2 = cnt, n - cnt
        
        answer = min(answer, abs(n1 - n2))
        
    return answer
        