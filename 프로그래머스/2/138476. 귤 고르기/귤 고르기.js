function solution(k, tangerine) {
    const map = new Map()
    
    for (let i = 0; i < tangerine.length; i++) {
        if (!map.get(tangerine[i])) {
            map.set(tangerine[i], 1)
        } else {
            map.set(tangerine[i], map.get(tangerine[i]) + 1)
        }
    }
    
    const tangerine_nums = Array.from(map, (a) => a[1])
    tangerine_nums.sort((a, b) => b - a)  // 내림차순

    let curr_k = 0
    for (let i = 0; i < tangerine_nums.length; i++) {
        curr_k += tangerine_nums[i]
        if (curr_k >= k) {
            return i + 1
        }
    }
}