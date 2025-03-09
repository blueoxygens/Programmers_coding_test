'''
당신은 온라인 게임을 운영하고 있습니다. 
같은 시간대에 게임을 이용하는 사람이 m명 늘어날 때마다 서버 1대가 추가로 필요합니다. 
어느 시간대의 이용자가 m명 미만이라면, 서버 증설이 필요하지 않습니다. 
어느 시간대의 이용자가 n x m명 이상 (n + 1) x m명 미만이라면 최소 n대의 증설된 서버가 운영 중이어야 합니다. 
한 번 증설한 서버는 k시간 동안 운영하고 그 이후에는 반납합니다. 
예를 들어, k = 5 일 때 10시에 증설한 서버는 10 ~ 15시에만 운영됩니다.
하루 동안 모든 게임 이용자가 게임을 하기 위해 서버를 최소 몇 번 증설해야 하는지 알고 싶습니다. 
같은 시간대에 서버를 x대 증설했다면 해당 시간대의 증설 횟수는 x회입니다.

0시에서 23시까지의 시간대별 게임 이용자의 수를 나타내는 1차원 정수 배열 players, 
서버 한 대로 감당할 수 있는 최대 이용자의 수를 나타내는 정수 m, 
서버 한 대가 운영 가능한 시간을 나타내는 정수 k가 주어집니다. 
이때, 모든 게임 이용자를 감당하기 위한 최소 서버 증설 횟수를 return 하도록 solution을 완성해 주세요.
'''

# m, k = 1
# k = 1
# else

import math
from collections import deque

def solution(players, m, k):
    answer = 0  # 최소 서버 증설 횟수
    active_servers = deque()  # 운영 중인 서버의 종료 시간을 관리하는 큐

    for time in range(len(players)):  # 0시부터 23시까지 순회
        # 현재 시간에 만료된 서버 반납
        while active_servers and active_servers[0] == time:
            active_servers.popleft()
        
        # 현재 운영 중인 서버가 감당할 수 있는 최대 인원
        max_capacity = len(active_servers) * m + m
        additional_servers = 0
        # 현재 인원을 감당할 수 없는 경우 추가 증설 필요
        if players[time] >= max_capacity:
            if m == 1:
                additional_servers = players[time] - max_capacity + 1
            elif players[time] - max_capacity == 0:
                additional_servers = 1
            elif (players[time] - max_capacity) % m == 0:
                additional_servers = math.ceil((players[time] - max_capacity) / (m-1))
            else:
                additional_servers = math.ceil((players[time] - max_capacity) / m)
            answer += additional_servers
            
            # 추가된 서버의 종료 시간을 큐에 저장
            for _ in range(additional_servers):
                active_servers.append(time + k)
            print(f'{players[time]},{max_capacity},{additional_servers}')
    return answer

solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5)
print('')
solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1)
print('')
solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1)

#딱 한 케이스 틀렸다 왜 그럴까?