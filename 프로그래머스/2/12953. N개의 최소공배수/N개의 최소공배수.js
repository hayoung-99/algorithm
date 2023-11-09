function getGCD(a, b) {
    let r
    while (b !== 0) {
        r = a % b
        a = b
        b = r
    }

    return a    
}


function getLCM(a, b) {
    return (a * b) / getGCD(a, b)
}


function solution(arr) {
    let currLCM = arr[0]
    for (let i = 0; i < arr.length - 1; i++) {
        currLCM = getLCM(currLCM, arr[i+1])
    }
    
    return currLCM
}
