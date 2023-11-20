def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        filltered_skill = []
        for s in st:
            if skill.find(s) != -1:
                filltered_skill.append(s)
        tree = "".join(filltered_skill)
        
        if skill[0 : len(tree)] == tree:
            answer += 1
            
    return answer