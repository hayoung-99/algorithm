const MISS = 5, HIT = 1
function solution(cacheSize, cities) {
    if (cacheSize === 0) {
        return (cities.length * MISS)
    }
    
    const cache = []
    let answer = 0
    
    cities.forEach((item) => {
        const city = item.toUpperCase()
        const idx = cache.indexOf(city)
        
        if (idx === -1) {
            if (cache.length === cacheSize) {
                cache.shift()
            }
            answer += MISS
        } else {
            cache.splice(idx, 1)
            answer += HIT
        }
        cache.push(city)
    })
    
    return answer
}