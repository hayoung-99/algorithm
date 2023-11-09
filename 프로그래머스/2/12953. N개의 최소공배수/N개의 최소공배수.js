function getLCM(a, b) {
    if (b % a === 0) {
        return b
    }
    
    max = a * b
    for (let i = b; i <= max; i++) {
        if (i % a === 0 && i % b === 0) {
            return i
        }
    }
}

function solution(arr) {
    arr.sort((a, b) => a < b)
    
    let currLCM = arr[0]
    for (let i = 0; i < arr.length - 1; i++) {
        currLCM = getLCM(currLCM, arr[i+1])
    }
    
    return currLCM
}