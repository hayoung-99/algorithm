import math

def solution(progresses, speeds):
    # 남은 개발 일수 구하기
    days = []
    for progress, speed in zip(progresses, speeds):
        rest_days = math.ceil((100 - progress) / speed)
        days.append(rest_days)
        
    # 날마다 배포되는 기능 수 구하기
    answer = []
    temp_size = days[0]
    temp_length = 1
    
    for i in range(1, len(days)):
        if temp_size >= days[i]:
            temp_length += 1
            
        else:
            answer.append(temp_length)
            temp_length = 1
            temp_size = days[i]

        # 마지막 배포인 경우
        if i == len(days) - 1:
            answer.append(temp_length)
        
    return answer
