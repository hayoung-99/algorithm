from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([])
    
    idx = 0
    total_time = 1 # answer
    curr_weights = truck_weights[idx]
    
    q.append((truck_weights[idx], 1))
    idx += 1
    
    while idx < len(truck_weights):
        total_time += 1
        for i, truck_info in enumerate(q):
            w, t = truck_info
            q[i] = (w, t + 1)
            
        # 예외처리) 1초 후 도로를 다 건넌 트럭이 있는 경우 확인
        if q[0][1] == bridge_length + 1: 
            w, _ = q.popleft()
            curr_weights -= w
            
        curr_truck = truck_weights[idx]
            
        if curr_weights + curr_truck > weight or len(q) == bridge_length:
            # 현재 truck을 도로 위에 올릴 수 있도록 앞의 truck 보내기
            while curr_weights + curr_truck > weight or len(q) == bridge_length:
                rest_time = bridge_length + 1 - q[0][1]
                
                for i, truck_info in enumerate(q):
                    w, t = truck_info
                    q[i] = (w, t + rest_time)
                
                w, _ = q.popleft()
                curr_weights -= w
                total_time += rest_time
        
        # 현재 truck을 도로 위에 올리기
        q.append((curr_truck, 1))
        curr_weights += curr_truck
        
        idx += 1    
        
    # 도로를 달리는 마지막 트럭까지 모두 빼기
    rest_time = bridge_length + 1 - q[-1][1]
    total_time += rest_time
    
    return total_time
    
    
            
        