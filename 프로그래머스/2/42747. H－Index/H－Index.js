function solution(citations) {
    let answer = 0
    
    const max_citations = Math.max(...citations)
    for (let h = 1; h <= max_citations; h++) {
        let curr = 0
        for (let c = 0; c < citations.length; c++) {
            if (citations[c] >= h) {
                curr += 1
            }
        }
        
        if (curr >= h) {
            answer = h
        }
    }
    
    return answer
    }