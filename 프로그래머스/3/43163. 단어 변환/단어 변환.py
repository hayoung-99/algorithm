def checkValid(word, target):
    diff = 0
    for i in range(len(word)):
        if word[i] != target[i]:
            diff += 1
        if diff > 1:
            return False
    return True
            

def makeComb(target, comb, words):
    global answer
    
    # 현재 word와 target 비교
    # 현재 comb 다음에 target이 올 수 있다면 더 탐색하지 않아도 되므로 종료
    last_word = comb[-1]
    if checkValid(last_word, target):
        print(comb)
        answer = min(answer, len(comb))
        return 
    
    for word in words:
        copy = list(words)
        
        if checkValid(last_word, word):
            comb.append(word)
            copy.remove(word)
            makeComb(target, comb, copy)
            comb.pop()
    

def solution(begin, target, words):
    global answer
    answer = 50
    
    if target not in words:
        return 0
    
    makeComb(target, [begin], words)
    
    return answer