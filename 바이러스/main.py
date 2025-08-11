import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())
computers = [ [-1] * (N+1) for _ in range(N+1)]

for i in range(M):
    one, two = map(int, input().strip().split(" "))
    computers[one][two], computers[two][one] = 1, 1

visited = set()
visited.add(1)
q = deque([1])
count = 0

while q : 
    cn = q.popleft()
    # print(f'현재노드 : {cn}')
    for pivot, n in enumerate(computers[cn]):
        if n == 1 and pivot not in visited:
            q.append(pivot)
            visited.add(pivot)
    count += 1
    

print(count-1)