function solution(k, tangerine) {
    const obj = {}
    
    for (let i = 0; i < tangerine.length; i++) {
        if (!(tangerine[i] in obj)) {
            obj[tangerine[i]] = 1
        } else {
            obj[tangerine[i]] += 1
        }
    }
    
    const values = Object.values(obj) 
    values.sort((a, b) => a - b)
    
    let curr_reduce = 0
    let reduce = tangerine.length - k
    for (let i = 0; i < values.length; i++) {
        curr_reduce += values[i]
        if (curr_reduce > reduce) {
            return (values.length - i)
        }
    }
    
    return 0
}