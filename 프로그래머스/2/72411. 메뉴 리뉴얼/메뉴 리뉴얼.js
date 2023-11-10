let answer = []

function combination(s, n, idx, curr, result) {
    if (curr.length === n) {
        result.push(curr)
        return
    } 
    
    if (idx === s.length || curr.length > n) {
        return
    }
    
    for (let i = idx; i < s.length; i++) {
        combination(s, n, i + 1, curr + s[i], result)
    }
}


function solution(orders, course) {
    const map = new Map()
    
    // 1. 각 order마다 오름차순 정렬 ex. 'xw' => 'wx'
    const orders_sort = []
    for (const order of orders) {
        let orderToArr = [...order]
        orderToArr.sort()
        orders_sort.push(orderToArr.join(''))
    }
    
    // 2. 각 order마다 구할 수 있는 조합을 map으로 관리
    for (let order of orders_sort) {
        for (const i of course) {
            let temp = []
            combination(order, i, 0, "", temp)
            
            for (const t of temp) {
                if (!map.get(t)) {
                    map.set(t, 1)
                } else {
                    map.set(t, map.get(t) + 1)
                }
            }
        }
    }
    
    // 3. 코스요리 개수와 일치하면서 2명 이상이 주문을 했는지 확인
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
    
    // 4. 오름차순 정렬
    answer.sort()
    
    return answer
}