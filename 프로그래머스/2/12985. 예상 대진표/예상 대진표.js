function swap(a, b) {
    return [b, a]
}


function solution(n,a,b)
{
    if (a > b) {
        [a, b] = swap(a, b)
    }
    let curr_round = 1;
    
    while (1) {
        // 현재 라운드에서 만나는 경우
        if (a % 2 === 1 && a + 1 === b) break
        
        // 다음 부여받을 번호 결정
        if (a % 2 === 0) {
            a /= 2
        } else {
            a = parseInt(a / 2) + 1
        }
        
        if (b % 2 === 0) {
            b /= 2
        } else {
            b = parseInt(b / 2) + 1
        }
        
        curr_round++
    }

    return curr_round;
}