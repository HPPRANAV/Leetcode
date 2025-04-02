class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len((nums))):   
                    max_val = max(max_val, calc(nums[i], nums[j], nums[k]))

        return max_val


def calc(num1, num2, num3):
    value = ((num1 - num2) * num3)
    if value > 0:
        return value
    return 0