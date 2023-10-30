def recursion(numbers, target, idx, curr):
    global answer
        
    if idx == len(numbers):
        if curr == target:
            answer += 1
        return
    
    # + 연산
    recursion(numbers, target, idx+1, curr + numbers[idx])
    
    # - 연산
    recursion(numbers, target, idx+1, curr - numbers[idx])


def solution(numbers, target):
    global answer
    answer = 0
    
    recursion(numbers, target, 0, 0)
    
    return answer