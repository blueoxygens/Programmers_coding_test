class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        def expand(left, right):
            # 좌우로 확장하며 팰린드롬인지 확인
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 팰린드롬인 부분만 반환
            return s[left + 1:right]

        ans = ""
        for i in range(len(s)):
            # 1. 홀수 길이 팰린드롬 (중심이 문자 1개: 'aba')
            res1 = expand(i, i)
            # 2. 짝수 길이 팰린드롬 (중심이 문자 사이: 'abba')
            res2 = expand(i, i + 1)
            
            # 가장 긴 것 업데이트
            ans = max(ans, res1, res2, key=len)
            
        return ans