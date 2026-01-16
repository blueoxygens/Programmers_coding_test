from collections import defaultdict, deque

def determine_oe(root, edges, flag):
    if flag:
        if root % 2 == 0:
            if len(edges[root]) % 2 == 0:
                return 0 #짝수 노드
            else:
                return 1 #역짝수 노드
        else:
            if len(edges[root]) % 2 == 1:
                return 0 #홀수 노드
            else:
                return 1 #역홀수 노드
    else:
        if root % 2 == 0:
            if (len(edges[root])-1) % 2 == 0:
                return 0 #짝수 노드
            else:
                return 1 #역짝수 노드
        else:
            if (len(edges[root])-1) % 2 == 1:
                return 0 #홀수 노드
            else:
                return 1 #역홀수 노드


def solution(nodes, edges):
    answer = [0,0]
    es = defaultdict(list, {k:[] for k in nodes})
    
    for n1, n2 in edges:
        es[n1].append(n2)
        es[n2].append(n1)
        
    record = [[-1] * 1000001 for _ in range(2)]
    
    for n in nodes:
        q = deque()
        visited = set()
        
        q.append(n)
        visited.add(n)
        comp = 0
        ans = 0
        
        #root의 노드 종류 기록
        if record[0][n] != -1:
            comp = record[0][n]
        else:
            comp = determine_oe(n, es, True)
            record[0][n] = comp
        
        #bfs 돌리기
        while q:
            t = q.popleft()
            for tc in es[t]:
                if tc not in visited:
                    q.append(tc)
                    visited.add(tc)
                    if record[1][tc] != -1:
                        if comp == record[1][tc]:
                            continue
                        else:
                            ans = -1
                            break
                    else:
                        record[1][tc] = determine_oe(tc,es, False)
                        if comp != record[1][tc]:
                            ans = -1
                            break
                        continue
            if ans != -1:
                ans = comp
        if ans >= 0:
            answer[ans] += 1
    return answer