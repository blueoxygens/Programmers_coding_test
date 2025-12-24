import sys

from collections import deque



sys.stdin = open("input.txt", "r")



T = int(sys.stdin.readline())



for tc in range(1, T+1):

    x, y = map(int, sys.stdin.readline().strip().split(" "))

    # print(f'{x} {y}')

    target = y-1

    ans = 2**31

    q = deque()

    q.append((x,0,0))

    visited = set()

    visited.add((x,0,0))

    dyear = [-1,0,1]

    

    while q:

        cindex, year, total = q.popleft()

        if cindex not in visited and cindex < target:

            for dy in dyear:

                tyear = year + dy

                if tyear > 0:

                    q.append((cindex + tyear, tyear, total+1))

                    visited.add((cindex,tyear, total+1))

        if cindex == target:

            ans = min(ans, total+1)

    

    print(ans)