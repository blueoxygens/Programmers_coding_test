from collections import deque

def solution(players, callings):
    for name in callings:
        index = players.index(name)
        #index가 문제.. 시간 복잡도가 N^2이 된다.
        front = players[:index-1]
        front.append(players[index])
        rear = deque(players[index+1:])
        rear.appendleft(players[index-1])
        front.extend(list(rear))
        players = front
    return players