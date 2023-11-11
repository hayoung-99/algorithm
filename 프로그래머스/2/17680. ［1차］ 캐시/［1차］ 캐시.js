const CACHE_HIT = 1
const CACHE_MISS = 5

function solution(cacheSize, cities) {    
    if (cacheSize === 0) {
        return (cities.length * CACHE_MISS)
    }
    
    const cache = []
    let total_time = 0
    let used_time = 0
    
    for (const curr of cities) {
        const city = curr.toUpperCase()
        if (cache.length === 0) {
            cache.push([city, used_time++])
            total_time += CACHE_MISS
        } else {
            let isInCache = false
            for (let i = 0; i < cache.length; i++) {
                if (cache[i][0] === city) {
                    total_time += CACHE_HIT
                    isInCache = true
                    cache[i] = [city, used_time++]
                }
            }
            if (!isInCache) {
                if (cache.length < cacheSize) {
                    cache.push([city, used_time++])
                } else {
                    // 가장 오랫동안 쓰지 않은 캐시 교체
                    let most_stale_time = cities.length
                    let most_stale_idx
                    for (let i = 0; i < cache.length; i++) {
                        if (most_stale_time > cache[i][1]) {
                            most_stale_time = cache[i][1]
                            most_stale_idx = i
                        }
                    }
                    cache[most_stale_idx] = [city, used_time++]
                }
                total_time += CACHE_MISS
            }
        } 
    }
    return total_time
}