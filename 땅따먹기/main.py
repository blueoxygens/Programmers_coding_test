def solution(land):
    answer = 0
    #memoization
    memo = [[0] * len(land[0]) for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(4):
            if i == 0:
                memo[i][j] = land[i][j]
            elif memo[i-1][j] != 0:
                max_sum = 0
                for k in range(4):
                    if k != j and max_sum < memo[i-1][k]:
                        max_sum = memo[i-1][k]
                memo[i][j] = land[i][j] + max_sum
    answer = max(memo[len(land)-1])
    return answer