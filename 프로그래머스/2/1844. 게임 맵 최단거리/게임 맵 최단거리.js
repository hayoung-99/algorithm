function inRange(x, y, col, row) {
    return ((0 <= x && x < col) && (0 <= y && y < row))
}


function bfs(maps) {
    const col = maps.length
    const row = maps[0].length
    
    // // 도착점이 막혀 있는 경우    
    // if (maps[col - 2][row - 1] === 0 && maps[col - 1][row - 2] === 0) {
    //     return -1
    // }
    
    // 큐 생성
    let start = 0
    let end = 0
    let queue = Array.from({ length: col * row }, () => 0)
    let items = 0
    
    // visited 초기화
    const visited = []
    for (let x = 0; x < col; x++) {
        visited.push(Array.from({ length: row }, () => 0))
    }
    
    // (0, 0) start
    queue[end] = [0, 0, 1]
    visited[0][0] = 1
    end = (end + 1) % (col * row)
    items = items + 1
    
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while (items !== 0) {
        // pop
        const [x, y, d] = queue[start]
        start = (start + 1) % (col * row)
        items = items - 1
                
        if (x === col - 1 && y === row - 1) {
            return d
        }
        
        for (let i = 0; i < 4; i++) {
            const nx = x + directions[i][0]
            const ny = y + directions[i][1]
            
            if (inRange(nx, ny, col, row) && !visited[nx][ny] && maps[nx][ny] !== 0) {
                // push
                queue[end] = [nx, ny, d + 1]
                end = (end + 1) % (col * row)
                visited[nx][ny] = 1
                items = items + 1
            }
        }   
    }
    return -1
}


function solution(maps) {
    const answer = bfs(maps)
    return answer;
}