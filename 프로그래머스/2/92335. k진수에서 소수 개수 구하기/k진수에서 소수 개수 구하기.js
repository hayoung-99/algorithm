function isPrime(n) {
    if (n === 1) {
        return false
    }
    
    for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
        if (n % i === 0) {
            return false
        }
    }
    return true
}


function solution(n, k) {
    const nToK = n.toString(k)
    const splitZero = nToK.split("0")
    
    let answer = 0
    for (const sz of splitZero) {
        if (sz === '') {
            continue
        }
        
        if (isPrime(parseInt(sz)) === true) {
            answer += 1
        }
    }
    
    return answer
}