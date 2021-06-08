def solution(genres, plays):
    answer = []
    data = {}
    datas = {}
    for i in range(len(genres)):
        if genres[i] not in data:
            data[genres[i]] = 0
            datas[genres[i]] = []
        data[genres[i]] += plays[i]
        datas[genres[i]].append((i, plays[i]))

    from collections import Counter

    cnt = Counter(data)
    # most_common 높은 순으로 list(tuple) 형태로 반환
    for key, sum in cnt.most_common():
        dd = datas[key]
        # list안에 tuple을 두번째 값으로 내림차순 정렬 
        dd.sort(key=lambda v:v[1], reverse=True)
        count = 0
        for i, v in dd:
            answer.append(i)
            count += 1
            if count == 2:
                break
        
    return answer

# 
# 장르 genres = ["classic", "pop", "classic", "classic", "pop"]
# 재생횟수 plays = [500, 600, 150, 800, 2500]
# output = [4, 1, 3, 0]
#