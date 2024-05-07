import copy 

answer = []
ANSWER_LENGTH = 0

def goNext(loadmap, curr, currAnswer):
    # 더이상 갈 수 없을 때 check answer
    if curr not in loadmap or len(loadmap[curr]) == 0:
        updateAnswer(currAnswer)
        return;
    
    copy_loadmap = copy.deepcopy(loadmap)
    for i, toGo in enumerate(copy_loadmap[curr]):
        # 1) 현재 공항 방문하기
        currAnswer.append(toGo)
        loadmap[curr] = loadmap[curr][:i] + loadmap[curr][i+1:]
        goNext(loadmap, toGo, currAnswer)
        
        # 2) 현재 공항 미방문하고, 다음 공항으로 가기
        currAnswer.pop()
        loadmap[curr].insert(i, toGo)
        

def updateAnswer(newAnswer):
    global answer 
    
    if len(newAnswer) != ANSWER_LENGTH:
        return;
    
    if len(answer) == 0:
        answer = copy.deepcopy(newAnswer)
        return;
    
    for i in range(ANSWER_LENGTH):
        curr_answer_item = answer[i]
        curr_new_answer_item = newAnswer[i]
        
        for k in range(3):
            if curr_answer_item[k] > curr_new_answer_item[k]:
                answer = copy.deepcopy(newAnswer)
                return;
            elif curr_answer_item[k] < curr_new_answer_item[k]:
                return;
            
    
def solution(tickets):
    global answer, ANSWER_LENGTH
    
    loadmap = {}
    ANSWER_LENGTH = len(tickets) + 1
    for ticket in tickets:
        start, end = ticket
        
        if start not in loadmap:
            loadmap[start] = []
        loadmap[start].append(end)
            
    goNext(loadmap, 'ICN', ['ICN'])
    return answer