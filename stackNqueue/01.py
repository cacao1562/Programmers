def solution(progresses, speeds):
    answer = []
    from math import ceil
    # ceil 올림 
    temp = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    # -((p-100) // s) 올림 없이 사용 
    # temp = list(map(lambda x: (-((progresses[x]-100) // speeds[x])), range(len(progresses))))

    cnt = 0
    p = temp[0]
    for i in range(len(temp)):
        if p < temp[i]:
            answer.append(cnt)
            p = temp[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)
    
    return answer
    
#
# 작업 진도 progresses = [95, 90, 99, 99, 80, 99]
# 개발 속도 speeds = [1, 1, 1, 1, 1, 1]
# output = [1, 3, 2]
#
