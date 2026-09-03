class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [0] * n
        dp[0], dp[1], dp[2] = 1, 2, 3
        i = 3
        while i < n:
            before_prev = dp[i-2]
            prev = dp[i-1]
            current = before_prev + prev
            dp[i] = current
            i += 1
        count = dp.pop()   
        return count