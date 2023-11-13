function getSet(str) {
    const answer = []
    const upper = str.toUpperCase()
    
    for (let i = 0; i < upper.length - 1; i++) {
        if (('A' <= upper[i] && upper[i] <= 'Z') && ('A' <= upper[i + 1] && upper[i + 1] <= 'Z')) {
            answer.push(upper.substr(i, 2))
        }
    }
    
    return answer
}

function solution(str1, str2) {
    const multi_set1 = getSet(str1)
    const multi_set2 = getSet(str2)
    const set1 = new Set(multi_set1)
    const set2 = new Set(multi_set2)
    
    // 공집합인 경우
    if (set1.size === 0 && set2.size === 0) {
        return (1 * 65536)
    }
    
    // 합집합 / 교집합 구하기
    const union = new Set()
    const intersection = new Set()
    
    set1.forEach((elem) => {
        union.add(elem)
        if (set2.has(elem)) {
            intersection.add(elem)
        }
    })
    
    set2.forEach((elem) => {
        union.add(elem)
    })
    
    console.log(union, intersection)
    
    // 각 multi set에 원소 개수 구하기
    // 1. 합집합
    let union_cnt = 0
    for (const u of union) {
        const multi_set1_cnt = multi_set1.reduce((cnt, elem) => cnt + (elem === u), 0)
        const multi_set2_cnt = multi_set2.reduce((cnt, elem) => cnt + (elem === u), 0)
        
        union_cnt = union_cnt + Math.max(multi_set1_cnt, multi_set2_cnt)
    }
    
    // 2. 교집합
    let intersection_cnt = 0
    for (const i of intersection) {
        const multi_set1_cnt = multi_set1.reduce((cnt, elem) => cnt + (elem === i), 0)
        const multi_set2_cnt = multi_set2.reduce((cnt, elem) => cnt + (elem === i), 0)
        
        intersection_cnt = intersection_cnt + Math.min(multi_set1_cnt, multi_set2_cnt)
    }
    
    return Math.floor((intersection_cnt / union_cnt) * 65536)
}