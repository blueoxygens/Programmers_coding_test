from collections import deque

n, m, k = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(n)]
trees_input = [tuple(map(int, input().strip().split())) for _ in range(m)]

# grid[r][c][나이] = 나무 개수
from collections import defaultdict
grid_trees = [[defaultdict(int) for _ in range(n+1)] for _ in range(n+1)]
for x, y, z in trees_input:
    grid_trees[x][y][z] += 1

grid = [[5] * (n+1) for _ in range(n+1)]
dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for year in range(k):
    new_grid_trees = [[defaultdict(int) for _ in range(n+1)] for _ in range(n+1)]
    
    # 봄 + 여름
    for r in range(1, n+1):
        for c in range(1, n+1):
            dead_nutrition = 0
            for z in sorted(grid_trees[r][c].keys()):
                count = grid_trees[r][c][z]
                # 몇 개나 살 수 있는지
                can_live = min(count, grid[r][c] // z)
                grid[r][c] -= can_live * z
                if can_live > 0:
                    new_grid_trees[r][c][z+1] += can_live
                dead = count - can_live
                dead_nutrition += dead * (z // 2)
            grid[r][c] += dead_nutrition  # 여름

    # 가을
    for r in range(1, n+1):
        for c in range(1, n+1):
            for z, count in new_grid_trees[r][c].items():
                if z % 5 == 0:
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 1 <= nr <= n and 1 <= nc <= n:
                            new_grid_trees[nr][nc][1] += count

    # 겨울
    for r in range(1, n+1):
        for c in range(1, n+1):
            grid[r][c] += A[r-1][c-1]

    grid_trees = new_grid_trees

# 총 나무 수
ans = 0
for r in range(1, n+1):
    for c in range(1, n+1):
        ans += sum(grid_trees[r][c].values())

print(ans)