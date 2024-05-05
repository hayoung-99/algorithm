def getAnswer(arr):
    n = len(arr)
    answer = []
    
    x = 0
    y = 0
    while x < n:
        item = arr[x][y]
        if item != 0:
            answer.append(item)
            y += 1
        else:
            x += 1
            y = 0
            
        if y == n:
            break
            
    return answer
    

def getTotal(n):
    total = 0
    for i in range(1, n+1):
        total += i
        
    return total


def canGo(arr, x, y):
    n = len(arr)
    
    isInRange = 0 <= x < n and 0 <= y < n
    return isInRange and arr[x][y] == 0
    

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)] 
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    curr_d = 0
    curr_x = 0
    curr_y = 0
    item = 1
    total = getTotal(n)
    for item in range(1, total + 1):
        answer[curr_x][curr_y] = item
        temp_x = curr_x + dx[curr_d]
        temp_y = curr_y + dy[curr_d]
        
        if (not canGo(answer, temp_x, temp_y)):
            curr_d = (curr_d + 1) % 3
            curr_x += dx[curr_d]
            curr_y += dy[curr_d]
        else:
            curr_x = temp_x
            curr_y = temp_y
            
    return getAnswer(answer)
        
    