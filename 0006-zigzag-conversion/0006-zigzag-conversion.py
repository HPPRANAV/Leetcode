class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        nums = [[] for _ in range(numRows)]
        x = 0
        direction = 1
        for char in s:
            nums[x].append(char)

            if x == 0:
                direction = 1
            if x == numRows-1:
                direction = -1
            
            x+=direction

        string = ''
        for word in nums:
            for char in word:
                string+=char
        
        return string

        
                          