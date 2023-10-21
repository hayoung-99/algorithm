def solution(n):
    stack = []
    
    curr = n
    while curr >= 1:
        if curr % 3 == 0:
            stack.append(3)
            curr = (curr // 3) - 1
        else:
            stack.append(curr % 3)
            curr //= 3
            
    answer = ""
    mapper = ["1", "2", "4"]
    for i in stack[::-1]:
        answer += mapper[i-1]
            
    return answer