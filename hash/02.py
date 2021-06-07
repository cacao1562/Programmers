def solution(phone_book):
    answer = True
    dic = {}
    for number in phone_book:
        dic[hash(number)] = number
    for phone in phone_book:
        for key in dic.keys():
            if dic[key] == phone:
                pass
            elif dic[key].startswith(phone):
                return False
    return answer

#
# 전화번호부 phoneBook = ["119", "97674223", "1195524421"]
# output = False
#