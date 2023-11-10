function solution(arr1, arr2) {
    const answer = []
    for (let i = 0; i < arr1.length; i++) {
        answer.push([])
    }
    
    for (let x = 0; x < arr1.length; x++) {
        for (let k = 0; k < arr2[0].length; k++) {
            let curr = 0
            for (let y = 0; y < arr1[0].length; y++) {
                curr += (arr1[x][y] * arr2[y][k])
            }
            answer[x].push(curr)
        }
    }
    
    return answer;
}