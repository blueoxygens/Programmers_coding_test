import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(" ")))

B = sorted(A)

h = defaultdict(deque)

for i, v in enumerate(B):
    h[v].append(i)

P = []

for i in A:
    P.append(h[i].popleft())

print(*P)