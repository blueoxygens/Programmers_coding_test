def solution(a, b):
    len_a, len_b = len(a), len(b)
    
    # DP 테이블 초기화 (0으로 채움)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    # DP 테이블 채우기
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:  # 같은 문자일 경우
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 다를 경우
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len_a][len_b]  # 최장 공통 부분 수열 길이 반환
