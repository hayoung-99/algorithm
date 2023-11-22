def getNextWord(curr, words):
    for word in words:
        cnt = 0
        for c, w in zip(curr, word):
            if c != w:
                cnt += 1
                
        if cnt == 1:
            yield word

            
def solution(begin, target, words):
    if target not in words:
        return 0
    
    levels = {begin: 0}
    q = [begin]
    
    while q:
        curr = q.pop(0)
        for nextWord in getNextWord(curr, words):
            if nextWord not in levels:
                levels[nextWord] = levels[curr] + 1
                q.append(nextWord)
                
    if target not in levels:
        return 0
    return levels[target]
    