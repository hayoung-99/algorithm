function solution(n, s) {
    if (n > s) {
        return [-1]
    }
    
    const answer = []
    let curr_n = n, curr_s = s

    while (curr_n > 0) {
        const curr = Math.ceil(curr_s / curr_n)
        
        answer.push(curr)
        
        curr_s -= curr
        curr_n -= 1
    }
    
    answer.sort((a, b) => a - b)
    
    return answer
}