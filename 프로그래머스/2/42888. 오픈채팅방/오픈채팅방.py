def printEnter(name):
    return f"{name}님이 들어왔습니다."
    
def printLeave(name):
    return f"{name}님이 나갔습니다."
    

def solution(record):
    answer = []
    names = {}
    
    for rec in record:
        commands = rec.split(' ')
        if commands[0] != 'Leave':
            names[commands[1]] = commands[2]
            
    for rec in record:
        commands = rec.split(' ')
        if commands[0] == 'Enter':
            answer.append(printEnter(names[commands[1]]))
        
        elif commands[0] == 'Leave':
            answer.append(printLeave(names[commands[1]]))
            
    return answer