def solution(phone_book):
    hashmap = {}
    for phone_num in phone_book: #폰넘버가 폰 북안에 있을 때, 해시맵
        hashmap[phone_num]=1
        
    for phone_num in phone_book:
        jubdoo = ""
        for number in phone_num:
            jubdoo += number
            print(jubdoo)
            if jubdoo in hashmap and jubdoo != phone_num:
                return False
    return True
