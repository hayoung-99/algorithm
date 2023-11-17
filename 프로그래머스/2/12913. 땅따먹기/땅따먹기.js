function solution(land) {
    const dp = Array.from(Array(land.length), () => Array(land[0].length).fill(0))
    
    for (let col = 0; col < 4; col++) {
        dp[0][col] = land[0][col]
    }
    
    for (let row = 1; row < land.length; row++) {
        for (let col = 0; col < 4; col++) {
               // col = 0 -> 1, 2, 3 => 1, 2, 3
                // 1 -> 0, 2, 3... => (2, 3, 4) % 4
                // 2 -> 0, 1, 3 => (3, 4, 5) % 4
            let plusNum = 0
            let temp = col
            while (plusNum < 3) {
                temp = (temp + 1) % 4
                dp[row][col] = Math.max(dp[row][col], dp[row - 1][temp])
                plusNum += 1
            }
            dp[row][col] += land[row][col]
        }
    }
    
    return Math.max(...dp[land.length - 1])
}