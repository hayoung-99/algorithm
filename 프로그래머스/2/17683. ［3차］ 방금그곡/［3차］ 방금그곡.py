import math

def calculatePlaytime(s, e):
    s_hour, s_minute = map(int, s.split(':'))
    e_hour, e_minute = map(int, e.split(':'))
    
    return (e_hour * 60 + e_minute) - (s_hour * 60 + s_minute)


def notesToArray(notes):
    arr = []
    idx = 0
    
    while idx < len(notes):
        if idx + 1 < len(notes) and notes[idx + 1] == '#':
            arr.append(notes[idx:idx+2])
            idx += 2
        else:
            arr.append(notes[idx])
            idx += 1
            
    return arr
        
    
def findall(target, notes):
    answer = []
    
    idx = 0
    while idx < len(notes):
        if notes[idx: idx + len(target)] == target:
            answer.append(idx)
            idx += len(target)
        else:
            idx += 1
            
        if idx + len(target) > len(notes):
            break
            
    return answer
    

def solution(m, musicinfos):
    musics = []
    
    for mi in musicinfos:
        s, e, name, notes = mi.split(',')
        playtime = calculatePlaytime(s, e)
        notes = notesToArray(notes)
        
        if playtime < len(notes):
            played_notes = ''.join(notes[:playtime])
        else:
            played_notes = ''.join(list(notes) * math.ceil(playtime / len(notes)))

        for offset in findall(m, played_notes):
            if offset + len(m) <= len(played_notes):
                if offset + len(m) == len(played_notes) or played_notes[offset + len(m)] != '#':
                    musics.append((playtime, name))
        
    musics.sort(key=lambda x: -x[0])
    
    if not musics:
        return "(None)"
    return musics[0][1]
         