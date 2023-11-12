function inRange(x, y) {
    return ((-5 <= x && x <= 5) && (-5 <= y && y <= 5))
}

function solution(dirs) {
    const visited = []
    for (let i = 0; i < 11; i++) {
        const col = Array.from({length: 11}, () => [0, 0, 0, 0])
        visited.push(col)
    }
    
    let curr_x = 0, curr_y = 0
    const mapper = {
        'U': [0, 1],
        'L': [-1, 0],
        'R': [1, 0],
        'D': [0, -1]
    }
    
    const visited_mapper = {
        'U': 0,
        'R': 1,
        'D': 2,
        'L': 3
    }
    
    let answer = 0
    for (const dir of dirs) {
        const [dx, dy] = mapper[dir]
        const nx = curr_x + dx, ny = curr_y + dy
        // console.log(`(${curr_x}, ${curr_y}) -> (${nx}, ${ny})`)
        
        // 더 이상 갈 수 없을 때
        if (!inRange(nx, ny)) {
            continue
        }
        
        // 처음 방문할 때
        if (!visited[curr_x + 5][curr_y + 5][visited_mapper[dir]]) {
            // console.log(`처음 가는 길: (${curr_x}, ${curr_y}) -> (${nx}, ${ny})`)
            answer += 1
            // 정방향
            visited[curr_x + 5][curr_y + 5][visited_mapper[dir]] = 1
            // 역방향
            visited[nx + 5][ny + 5][(visited_mapper[dir] + 2) % 4] = 1
        }
        
        curr_x = nx, curr_y = ny
    }
    
    return answer
}