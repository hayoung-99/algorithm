class Heap {
    constructor() {
        this.heap = []
    }
    
    top() {
        if (this.heap.length !== 0) {
            return this.heap[0]
        }
        return null
    }
    
    length() {
        return this.heap.length
    }
    
    swap(idx1, idx2) {
        const temp = this.heap[idx1]
        this.heap[idx1] = this.heap[idx2]
        this.heap[idx2] = temp
    }
    
    getNext(curr, left, right) {
        if (left >= this.heap.length) {
            return curr
        } else if (right < this.heap.length) {
            let next;
            if (this.heap[left] < this.heap[right]) {
                if (this.heap[curr] > this.heap[left]) {
                    return left
                } 
                return curr
            } else {
                if (this.heap[curr] > this.heap[right]) {
                    return right
                } 
                return curr
            }
        } else {
            if (this.heap[curr] > this.heap[left]) {
                return left
            } else {
                return curr
            }
        }
    }
    
    push(value) {
        this.heap.push(value)
        let child = this.heap.length - 1
        
        while (child !== 0) {
            let parent = Math.ceil(child / 2) - 1
            if (this.heap[parent] > this.heap[child]) {
                this.swap(parent, child)
                child = parent
            } else{
                break
            }
        }
    }
    
    pop() {
        if (this.heap.length === 0) {
            return null
        }
        
        const min = this.heap[0]
        
        this.heap[0] = this.heap[this.heap.length - 1]
        this.heap.pop()
        let curr = 0
        
        while (curr < this.heap.length) {
            const next = this.getNext(curr, (curr * 2) + 1, (curr * 2) + 2)
            if (this.heap[curr] > this.heap[next]) {
                this.swap(curr, next)
                curr = next
            } else {
                break
            }
        }
        return min
    }
    
    print() {
        console.log(this.heap)
    }
}


function solution(scoville, K) {
    const heap = new Heap()
    
    for (const sc of scoville) {
        heap.push(sc)
    }
    
    let answer = 0
    while (heap.length() > 1 && heap.top() < K) {
        answer += 1
        const min1 = heap.pop()
        const min2 = heap.pop()
        
        heap.push(min1 + (min2 * 2))
    }
    
    if (heap.top() < K) {
        return -1
    } 
    return answer
    
}