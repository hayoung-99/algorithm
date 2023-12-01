def isCorrect(s):
    stack = [s[0]]
    
    for i in range(1, len(s)):
        if s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])    
            
    if not stack:
        return True
    return False


def splitString(s):
    open_br, close_br = 0, 0
    u = ''
    
    for i, br in enumerate(s):
        if br == '(':
            open_br += 1
        else:
            close_br += 1
            
        if open_br == close_br:
            return (s[:i+1], s[i+1:])
        
        
def formatString(s):
    result = ''
    
    for br in s[1:-1]:
        if br == '(':
            result += ')'
        else:
            result += '('
            
    return result
            

def recursion(s):
    if s == '':
        return ''
    
    # u, v로 분리
    u, v = splitString(s)
    
    temp = recursion(v)
    if isCorrect(u):
        return u + temp
        
    else:
        return '(' + temp + ')' + formatString(u)
    

def solution(p):
    if isCorrect(p):
        return p
    
    return recursion(p)