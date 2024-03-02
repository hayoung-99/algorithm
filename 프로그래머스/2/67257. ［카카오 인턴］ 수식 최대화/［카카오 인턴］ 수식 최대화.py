import re
from itertools import permutations

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    
    if operator == '-':
        return a - b
    
    if operator == '*':
        return a * b
    

def solution(expression):
    numbers = list(map(int, re.split(r'-|\*|\+', expression)))
    operators = re.split(r'\d+', expression)[1:-1]
    cases = permutations(['*', '+', '-'])
    result = 0
    
    for case in cases:
        curr_numbers = numbers[:]
        curr_operators = operators[:]
        temp_numbers = []
        temp_operators = []
        
        for target_operator in case:
            for i in range(len(curr_operators)):
                if i == 0:
                    if curr_operators[i] == target_operator:
                        temp_numbers.append(calculate(curr_numbers[i], curr_numbers[i+1], target_operator))
                        continue
                    temp_numbers.append(curr_numbers[i])
                    temp_numbers.append(curr_numbers[i+1])
                    temp_operators.append(curr_operators[i])
                    continue
                    
                if curr_operators[i] == target_operator:
                    temp_numbers[-1] = calculate(temp_numbers[-1], curr_numbers[i+1], target_operator)
                else:
                    temp_numbers.append(curr_numbers[i+1])     
                    temp_operators.append(curr_operators[i])
                    
            curr_numbers = temp_numbers[:]
            curr_operators = temp_operators[:]
            temp_numbers = []
            temp_operators = []
            
            if len(curr_numbers) == 1:
                break

        result = max(result, abs(curr_numbers[0]))
                        
    return result
    