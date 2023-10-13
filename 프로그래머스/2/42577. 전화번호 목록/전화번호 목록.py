def solution(phone_book):
    phone_dict = {}
    
    phone_book.sort(key=len)
    min_length = len(phone_book[0])
    
    for phone_num in phone_book:
        min_length = min(min_length, len(phone_num))
        
    for phone_num in phone_book:
        idx = min_length - 1
        curr_partial = phone_num[:min_length]
        
        while idx < len(phone_num):
            if curr_partial in phone_dict:
                return False
            else:
                idx += 1
                if idx == len(phone_num): # 부분 집합을 끝까지 돌았음에도 접두어를 발견하지 못한 경우 -> 해당 번호도 dict에 추가
                    phone_dict[phone_num] = True
                    break
                curr_partial += phone_num[idx]
                    
    return True
        