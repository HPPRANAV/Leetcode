class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for lis in triangle:
            dp.append(lis)
        

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]