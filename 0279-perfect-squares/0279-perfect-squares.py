class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        i = 1
        while i*i <= n:
            nums.append(i*i)
            i+=1
        
        #print(nums)
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for num in nums:
                if i >= num:
                    dp[i] = min(dp[i], dp[i-num]+1)
        print(dp)
        return dp[n]