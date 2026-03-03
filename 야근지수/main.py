import heapq
def solution(n, works):
    answer = 0
    l = len(works)
    w = []
    for i in range(l):
        heapq.heappush(w,-1*works[i])
    # print(w)
    for i in range(n):
        t = heapq.heappop(w)
        if t == 0:
            return 0
            break
        heapq.heappush(w,t+1)

    for i in range(l):
        answer += heapq.heappop(w)**2
    return answer