class Solution:
    def reverse(self, x: int) -> int:
        string = ''
        limit= (2**31)
        num = str(x)
        for i in range(len(num)-1, -1, -1):
            string+=num[i]
        if x < 0:
            number = -int(string[:len(num)-1])
        else:
            number = int(string)
        
        if number > limit-1 or number < -limit:
            return 0
        return number