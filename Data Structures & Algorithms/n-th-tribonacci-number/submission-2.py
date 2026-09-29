class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * max(3, (n+1))
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        if len(dp) >= 4:
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]