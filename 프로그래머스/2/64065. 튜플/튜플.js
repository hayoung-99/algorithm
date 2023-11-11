function solution(s) {
    const tupleToArr = JSON.parse(s.replace(/{/g, '[').replace(/}/g, ']'))
    
    // 배열 크기 순서대로 정렬
    tupleToArr.sort((a, b) => a.length - b.length)
    
    const answer = []
    tupleToArr.forEach((arr) => {
        arr.forEach((item) => {
            if (!answer.includes(item)) {
                answer.push(item)
            }
        })
    })
    
    return answer
}