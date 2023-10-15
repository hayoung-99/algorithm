def calculateSet(i, k, dp): 
    n_set = set([])
    
    for num1 in dp[i]:
        for num2 in dp[k]:
            n_set.add(num1 * num2)
            n_set.add(num1 + num2)
            n_set.add(num1 - num2)
            if num2 != 0:
                n_set.add(num1 // num2)
    
    return n_set


def solution(N, number):
    result = [[]] + [[int(str(N) * i)] for i in range(1, 9)]
    
    if N == number:
        return 1
    
    for n in range(2, 9):
        temp_set = set(result[n])
        
        for i in range(1, n):
            temp_set.update(calculateSet(i, n-i, result))
        
        if number in temp_set:
            return n
        
        result[n] = list(temp_set)
    return -1