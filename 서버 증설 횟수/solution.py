def solution(players, m, k):
    answer = 0
    servers = [0]*(24+k)
    nowmax = m
    for i,p in enumerate(players):
        nowmax -= servers[i]*m
        if nowmax<=p:
            addservers = ((p-nowmax)//m)+1
            answer += addservers
            nowmax+=addservers*m
            servers[i+k]+=addservers
    return answer