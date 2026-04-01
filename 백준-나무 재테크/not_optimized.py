import sys
from collections import deque

sys.stdin = open("input.txt","r")

T= int(input())

for tc in range(1,T+1):
    print(f'test case:{tc}', end= " ")
    #init
    n, m, k = map(int, input().strip().split(" "))
    A = [list(map(int, input().strip().split(" "))) for _ in range(n)]
    trees = [tuple(map(int,input().strip().split(" "))) for _ in range(m)]
    trees.sort(key=lambda x:x[2])
    
    grid = [[5]*n for _ in range(n)]
    
    def spring(trees):
        q = deque(trees)
        live = []
        dead = []
        while q:
            r,c,z = q.popleft()
            if grid[r-1][c-1] >= z:
                grid[r-1][c-1] -= z
                live.append((r,c,z+1))
            else:
                dead.append((r,c,z))
        return live, dead
        
    def summer(dead):
        for r,c,z in dead:
            grid[r-1][c-1] += z//2
    
    def autumn(trees):
        arr = []
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for x,y,z in trees:
            if z % 5 == 0:
                for dr, dc in dirs:
                    nr = x + dr
                    nc = y + dc
                    if 1<=nr<=n and 1<=nc<=n:
                        arr.append((nr,nc,1))
        return arr
        
    def winter():
        for i in range(n):
            for j in range(n):
                grid[i][j] += A[i][j]
        
    for year in range(k):
        trees, dead = spring(trees)
        summer(dead)
        trees = autumn(trees)+trees
        trees.sort(key=lambda x: x[2])
        winter()
    
    print(len(trees))