function solution(want, number, discount) {
    const curr = new Map()
    
    // 열흘 간 세일 목록
    for (let i = 0; i < 10; i++) {
        if (!curr.get(discount[i])) {
            curr.set(discount[i], 1)
        } else {
            curr.set(discount[i], curr.get(discount[i]) + 1)
        }
    }
    
    // 첫 열흘에 모두 세일하는 경우
//     for (let i = 0; i < want.length; i++) {
//         if (curr.get(discount[want[i]]) >= number[i]) {
            
//         }
//     }
    let answer = 0
    for (let i = 0; i <= discount.length - 10; i++) {
        let isExist = true
        for (let k = 0; k < want.length; k++) {
            if (curr.get(want[k]) === undefined || curr.get(want[k]) < number[k]) {
                isExist = false
            }
        }
        
        if (isExist) {
            answer += 1
        }
        
        // 다음 날 이동
        if (!curr.get(discount[i + 10])) {
            curr.set(discount[i + 10], 1)
        } else {
            curr.set(discount[i + 10], curr.get(discount[i + 10]) + 1)
        }
        curr.set(discount[i], curr.get(discount[i]) - 1)
    }
    
    return answer
}