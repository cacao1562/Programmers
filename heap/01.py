import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    L = len(scoville)
    f = heapq.heappop(scoville)
    for i in range(1, L):
        s = heapq.heappop(scoville)
        f = heapq.heappushpop(scoville, f+s*2)
        if f>=K: return i
    return -1

#
# 매운 정도 scoville = [1, 2, 3, 9, 10, 12]
# 매운 지수 K = 7
# output = 2
#