function getManhattanDist(x1, y1, x2, y2) {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}


function solution(places) {
    
    const answer = []
    for (const place of places) {
        const pos = []
        for (let x = 0; x < 5; x++) {
            for (let y = 0; y < 5; y++) {
                if (place[x][y] === 'P') {
                    pos.push([x, y])
                }
            }
        }

        let isSafe = true
        for (let i = 0; i < pos.length - 1; i++) {
            for (let k = i + 1; k < pos.length; k++) {
                const [x1, y1] = pos[i]
                const [x2, y2] = pos[k]

                const dist = getManhattanDist(x1, y1, x2, y2) 

                // 바로 옆자리인 경우 X
                if (dist === 1) {
                    isSafe = false
                    console.log(x1, y1, x2, y2, '바로 옆자리')
                    break
                }

                // 거리가 2보다 큰 경우 O
                if (dist > 2) {
                    continue
                }

                // 거리가 2인 경우
                if (dist === 2) {
                    // 1. 사선으로 있는 경우
                    if (Math.abs(x1 - x2) === 1) {
                        // 왼쪽 하단
                        if (y1 - 1 === y2) {
                            if (place[x1][y1 - 1] !== "X" || place[x1 + 1][y1] !== "X") {
                                isSafe = false
                                break
                            } 
                        }
                        
                        // 오른쪽 하단
                        if (y1 + 1 === y2) {
                            if (place[x1 + 1][y1] !== "X" || place[x1][y1 + 1] !== "X") {
                                isSafe = false
                                break
                            } 
                        }
                    } 
                    
                    // 2. 일직선으로 있는 경우
                    else {
                        const dx = Math.abs(x1 - x2) / 2
                        const dy = Math.abs(y1 - y2) / 2
                        
                        if (place[x1 + dx][y1 + dy] !== "X") {
                            isSafe = false
                            break
                        }
                    }
                }
            }
            
            if (!isSafe) break
        }
        if (!isSafe) {
            answer.push(0)
        } else {
            answer.push(1)
        }
    }
    
    return answer
}