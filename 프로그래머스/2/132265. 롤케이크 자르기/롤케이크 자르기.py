def solution(topping):
    left = {}
    right = {}
    
    for t in topping:
        if t not in right:
            right[t] = 1 
        else:
            right[t] += 1
            
    answer = 0
    
    for cut in range(len(topping)):
        curr_topping = topping[cut]
        if curr_topping not in left:
            left[curr_topping] = 1
        else:
            left[curr_topping] += 1
        right[curr_topping] -= 1
        
        if right[curr_topping] == 0:
            del right[curr_topping]
            
        if len(left.keys()) == len(right.keys()):
            answer += 1
            
    return answer
        