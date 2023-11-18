function solution(n, lost, reserve) {
    // 빌려줘야 되는 학생 리스트와, 빌려줄 수 있는 학생 리스트
    const only_lost = lost.filter((x) => !reserve.includes(x))
    const can_reserve = reserve.filter((x) => !lost.includes(x))
    
    // 오름차순 정렬
    can_reserve.sort((a, b) => a - b)
    
    for (const res of can_reserve) {
        // 앞에 빌려주기
        const front = only_lost.indexOf(res - 1)
        if (front !== -1) {
            only_lost.splice(front, 1)
            continue
        }
        
        // 뒤에 빌려주기
        const back = only_lost.indexOf(res + 1) 
        if (back !== -1) {
            only_lost.splice(back, 1)
        }
    } 
    
    return (n - only_lost.length)
}