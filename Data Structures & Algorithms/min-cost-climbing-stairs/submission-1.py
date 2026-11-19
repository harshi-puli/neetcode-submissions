class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dp = [0] * len(cost)

        dp[0] = cost[0]

        if len(cost) > 1:
            dp[1] = cost[1]

            for i in range(1, len(cost)):
                curr_cost = cost[i]
                
                dp[i] = min(curr_cost + dp[i-1], curr_cost + dp[i-2])

            
            return min(dp[len(cost)-1], dp[len(cost)-2])

        return dp[len(cost)]