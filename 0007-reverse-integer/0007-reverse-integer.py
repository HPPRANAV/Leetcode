class Solution:
    def reverse(self, x: int) -> int:
        negative, signed = False, 1<<31
        if x < 0:
            negative = True
            x*=-1
        
        res = 0
        while x > 0:
            res*=10
            res+= x%10
            x = x//10
        
        if negative:
            res*= -1
        
        if res >= signed or res < (-signed):
            return 0
        
        return res