function solution(phone_book) {
    const map = new Map()
    phone_book.sort((a, b) => a.length - b.length)
    
    const start = phone_book[0].length - 1
    for (const phone of phone_book) {
        let curr = phone.substring(0, start)
        for (let i = start; i < phone.length - 1; i++) {
            curr = curr + phone[i]
            
            if (map.get(curr)) {
                return false
            }
        }
        map.set(phone, true)
    }
    
    return true
}