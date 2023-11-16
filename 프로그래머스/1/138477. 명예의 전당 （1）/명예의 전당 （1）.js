function solution(k, score) {
    const high_score_list = []
    const answer = []
    
    for (const s of score) {
        high_score_list.push(s)
        high_score_list.sort((a, b) => b - a)
        
        if (high_score_list.length > k) {
            high_score_list.pop()
        }
        
        answer.push(high_score_list[high_score_list.length - 1])
    }
    
    return answer;
}