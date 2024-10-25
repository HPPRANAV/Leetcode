class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}

        def memo(index):
            if index == len(nums):
                return True
            
            if index in dp:
                return dp[index]

            res = False

            if index < len(nums) - 1 and nums[index] == nums[index+1]:
                res = memo(index + 2)
            if index < len(nums)-2:
                if(nums[index] == nums[index+1] == nums[index+2]) or (nums[index]+1 == nums[index+1] and nums[index+1]+1 == nums[index+2]):
                    res = res or memo(index+3)
            
            dp[index] = res
            return res
        
        return memo(0)

        
            

              