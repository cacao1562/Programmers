def solution(clothes):
    from collections import Counter
    from functools import reduce
    # name 의상이름, kind 의상종류
    # 종류 카운팅 
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # x 누적자, y 현재값 , 순회가능한값, 초기값
    return answer
