import re

def solution(files):
    head_and_number = []
    for i, file in enumerate(files):
        # head, number 추출
        strings = re.split(r'[0-9]+', file)
        numbers = [num for num in re.split(r'[^0-9]+', file) if num != '']
        
        head_and_number.append((strings[0], int(numbers[0]), i))

    head_and_number.sort(key=lambda x: (x[0].upper(), x[1]))
    answer = []
    for han in head_and_number:
        answer.append(files[han[2]])
        
    return answer