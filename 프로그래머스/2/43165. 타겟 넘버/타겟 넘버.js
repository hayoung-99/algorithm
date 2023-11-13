let answer = 0

function recursion(target, numbers, idx, result) {
    if (idx === numbers.length) {
        if (result === target) {
            answer = answer + 1
        }
        return
    }
    
    // 1. 현재 수를 더하기
    recursion(target, numbers, idx + 1, result + numbers[idx])
    
    // 2. 현재 수를 빼기
    recursion(target, numbers, idx + 1, result - numbers[idx])
}

function solution(numbers, target) {
    recursion(target, numbers, 0, 0)
    
    return answer;
}