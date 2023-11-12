// 1. 가장 처음으로 오는 0을 1로 설정한다. 
// 2. 그 뒤의 (뒤가 있다면) 1을 0으로 바꾼다.
function getBit(n) {
    return ('0' + n.toString(2))
}


function getDecimal(bit) {
    let answer = 0
    let pow = 0
    for (let i = bit.length - 1; i >= 0; i--) {
        answer += Math.pow(2, pow) * bit[i]
        pow += 1
    }
    
    return answer
}


function solution(numbers) {
    const answer = [];
    
    for (const num of numbers) {
        const bit = getBit(num)
        
        // 1.
        const zero_idx = bit.lastIndexOf('0')
        let curr = bit.substring(0, zero_idx) + '1' + bit.substring(zero_idx + 1, bit.length)
        
        // 2.
        if (zero_idx !== bit.length - 1) {
            curr = curr.substring(0, zero_idx + 1) + '0' + curr.substring(zero_idx + 2, bit.length)
        }
        
        answer.push(getDecimal(curr))
    }
    
    return answer;
}