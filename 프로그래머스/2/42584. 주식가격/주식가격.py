# 현재 stack append하려는 price를 stack의 top과 비교하여
# 현재 price가 더 작은 경우 계속해서 stack을 pop해가며 "두 인덱스 차를 통해 기간을 구한다."
def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        while stack != [] and stack[-1][0] > prices[i]:
            _, pi = stack.pop()
            answer[pi] = i - pi
        stack.append((prices[i], i))
        
    for _, idx in stack:
        answer[idx] = len(prices) - 1 - idx
        
    return answer
    