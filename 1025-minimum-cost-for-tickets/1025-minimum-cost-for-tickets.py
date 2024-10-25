class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        days_set = set(days) 
        durations = [1, 7, 30] 

        for i in range(1, last_day + 1):
            if i not in days_set: 
                dp[i] = dp[i-1]
            else:
                cost1 = dp[max(0, i-1)] + costs[0]
                cost7 = dp[max(0, i-7)] + costs[1]
                cost30 = dp[max(0, i-30)] + costs[2]
                dp[i] = min(cost1, cost7, cost30)
        
        return dp[last_day]