from collections import deque

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack = deque()
    for i, w in enumerate(arr):
        if i == 0:
            stack.append(w)
        else:
            if stack:
                temp = stack.pop()
                if temp == w:
                    stack.append(w)
                else:
                    while stack:
                        stack.pop()
                    answer.append(temp)
                    stack.append(w)
            if i == len(arr)-1:
                answer.append(w)
    return answer