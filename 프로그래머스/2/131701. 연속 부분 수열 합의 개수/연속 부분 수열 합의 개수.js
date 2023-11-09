function shiftLeft(arr) {
    let temp = arr[0]
    
    for (let i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i+1]
    }
    
    arr[arr.length - 1] = temp
    
    return arr
}


function solution(elements) {
    const answer = new Set(elements)
    
    let shiftArray = [...elements]
    
    let num = 1
    while (num < elements.length) {
        shiftArray = shiftLeft(shiftArray)
        
        for (let k = 0; k < elements.length; k++) {
            elements[k] += shiftArray[k]
            answer.add(elements[k])
        }
            
        num += 1
    }
    
    return answer.size
}