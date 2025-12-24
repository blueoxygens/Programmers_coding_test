import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.read().split()
T = int(input[0])
pointer = 1

for _ in range(T):
    x = int(input[pointer])
    y = int(input[pointer+1])
    pointer += 2
    
    distance = y - x
    if distance == 0:
        print(0)
        continue
        
    k = int(distance**0.5)
    
    if k**2 == distance:
        print(2 * k - 1)
    elif k**2 < distance <= k**2 + k:
        print(2 * k)
    else:
        print(2 * k + 1)