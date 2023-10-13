def solution(phone_book):
    phone_dict = {}
    for phone_num in phone_book:
        phone_dict[phone_num] = True
        
    for phone_num in phone_book:
        curr = ""
        for num in phone_num:
            curr += num
            # curr의 접두어가 phone_dict에 있으면서 그 접두어가 자신 번호가 아닌 경우 => 접두사 발견!
            if curr in phone_dict and curr != phone_num:
                return False
            
    return True
            