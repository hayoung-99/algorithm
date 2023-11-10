let answer = []

function permutations(s, n, idx, curr, result) {
    if (curr.length === n) {
        result.push(curr)
        return
    } 
    
    if (idx === s.length || curr.length > n) {
        return
    }
    
    for (let i = idx; i < s.length; i++) {
        permutations(s, n, i + 1, curr + s[i], result)
    }
}


function solution(orders, course) {
    const map = new Map()
    
    const orders_sort = []
    for (const order of orders) {
        let orderToArr = [...order]
        orderToArr.sort()
        orders_sort.push(orderToArr.join(''))
    }
    
    for (let order of orders_sort) {
        for (const i of course) {
            let temp = []
            permutations(order, i, 0, "", temp)
            // console.log(order, i, temp)
            
            for (const t of temp) {
                if (!map.get(t)) {
                    map.set(t, 1)
                } else {
                    map.set(t, map.get(t) + 1)
                }
            }
        }
    }
    
    const info = new Map()
    for (const c of course) {
        let max = 0
        for (const [key, value] of map) {
            if (key.length === c && value >= 2) {
                max = Math.max(max, value)
            }
        }
        info.set(c, max)
    }
    
    const answer = []
    for (const [key, value] of info) {
        for (const [mk, mv] of map) {
            if (mk.length === key && mv === value) {
                answer.push(mk)
            }
        }
    }
    
    answer.sort()
    
    return answer
}