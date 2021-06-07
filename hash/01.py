def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer

#
# 참가자 participant = ["leo", "kiki", "eden"]
# 완주자 completion = ["eden", "kiki"]
# output = "leo"
#