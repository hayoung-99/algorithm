function solution(msg) {
    const map = new Map()
    
    // 색인 번호 생성
    for (let i = ('A').charCodeAt(); i <= ('Z').charCodeAt(); i++) {
        map.set(String.fromCharCode(i), i - ('A').charCodeAt() + 1)
    }
    
    const answer = []
    let curr_idx = 27
    let curr_msg
    for (let i = 0; i < msg.length; i++) {
        if (i === 0) {
            curr_msg = msg[0]
            continue
        }
        
        let next_msg = curr_msg + msg[i]
        if (!map.get(next_msg)) {
            map.set(next_msg, curr_idx++)
            answer.push(map.get(curr_msg))
            curr_msg = msg[i]
        } else {
            curr_msg = next_msg
        }
    }
    
    // 마지막으로 처리되지 않은 문자 처리
    answer.push(map.get(curr_msg))
    
    return answer
}