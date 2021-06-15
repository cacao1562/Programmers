def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        
        stack.append([i, prices[i]])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

#
# 주식가격 prices = [1, 2, 3, 2, 3]
# output = [4, 3, 1, 1, 0]
#