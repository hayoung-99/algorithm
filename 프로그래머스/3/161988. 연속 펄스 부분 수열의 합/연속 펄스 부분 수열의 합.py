def solution(sequence):
    minus_first = [-1 if i % 2 == 0 else 1 for i in range(len(sequence))]
    plus_first = [1 if i % 2 == 0 else -1 for i in range(len(sequence))]
            
    # dp
    dp_minus_first = [0 for _ in range(len(sequence))]
    dp_plus_first = [0 for _ in range(len(sequence))]
    
    for i in range(len(sequence)):
        if i == 0:
            dp_minus_first[0] = sequence[0] * -1
            dp_plus_first[0] = sequence[0]
            
        else:
            # minus_first
            curr_minus_first = sequence[i] * minus_first[i]
            if dp_minus_first[i-1] > 0:
                dp_minus_first[i] = dp_minus_first[i-1] + curr_minus_first
            else:
                dp_minus_first[i] = curr_minus_first
                
            # plus_first
            curr_plus_first = sequence[i] * plus_first[i]
            if dp_plus_first[i-1] > 0:
                dp_plus_first[i] = dp_plus_first[i-1] + curr_plus_first
            else:
                dp_plus_first[i] = curr_plus_first
                
    answer = -999999
    for m, p in zip(dp_minus_first, dp_plus_first):
        answer = max(answer, m, p)
        
    return answer
         