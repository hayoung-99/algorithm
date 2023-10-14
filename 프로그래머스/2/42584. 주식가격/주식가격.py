def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = []
    stack.append((prices[0], 0))  # (price, index)
    
    for i in range(1, len(prices)):
        curr_price = prices[i]

        while len(stack) > 0 and stack[-1][0] > curr_price:
            price, idx = stack.pop()
            answer[idx] += 1
            for sprice, sidx in stack:
                if price >= sprice:
                    answer[sidx] += 1
                
        stack.append((curr_price, i))
        
    
    # stack에 남아있는 price 처리
    if len(stack) > 1:
        total_length = len(stack)
        
        s = 0
        for price, idx in stack:
            answer[idx] += total_length - (s + 1)
            s += 1
                
    return answer
        
    