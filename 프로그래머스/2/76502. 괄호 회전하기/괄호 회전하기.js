function shiftLeft(arr) {
    return arr.substring(1, arr.length) + arr[0]
}


function solution(arr) {
    const open = ["{", "(", "["]
    const close = ["}", ")", "]"]
    
    let answer = 0
    let shift = 0
    let s = arr
    while (shift < arr.length) {
        const stack = []
        
        stack.push(s[0])
        for (let k = 1; k < s.length; k++) {
            if (open.includes(s[k])) {
                stack.push(s[k])
            } else {
                const idx = close.indexOf(s[k])
                if (stack[stack.length - 1] === open[idx]) {
                    stack.pop()
                } else {
                    stack.push(s[k])
                    break
                }
            }
        }
        
        if (stack.length === 0) {
            answer += 1
        }
        
        s = shiftLeft(s)
        shift += 1
    }
    
    return answer
}