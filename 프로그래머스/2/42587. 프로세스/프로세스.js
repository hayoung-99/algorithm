function solution(priorities, location) {
    const q = []
    const map = new Map()
    
    for (let i = 0; i < priorities.length; i++) {
        q.push([priorities[i], i])
        
        if (!map.get(priorities[i])) {
            map.set(priorities[i], 1)
        } else {
            map.set(priorities[i], map.get(priorities[i]) + 1)
        }
    }
    
    const nums = []
    for (const [k, v] of map) {
        nums.push([k, v])
    }
    
    nums.sort((a, b) => b[0] - a[0])
    
    let idx = 0
    let answer = 0
    while (q.length !== 0) {
        const item = q.shift()
        
        // 1) 현재 실행할 프로세스를 찾은 경우
        if (item[0] === nums[idx][0]) {
            answer = answer + 1
            // 1-1) 그 프로세스가 답인 경우 return
            if (item[1] === location) {
                return answer
            } else {
                // 1-2) nums와 idx 업데이트
                nums[idx] = [nums[idx][0], nums[idx][1] - 1]
                if (nums[idx][1] === 0) {
                    idx = idx + 1
                }
            }
        } else {
            // 2) 현재 실행할 프로세스가 아닌 경우
            q.push(item)
        }
    }
}
