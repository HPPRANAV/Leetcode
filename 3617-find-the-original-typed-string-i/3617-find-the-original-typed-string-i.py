class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)

        i=0
        count=1
        while i < n:
            j=0
            while j < n:
                if j+1 < n and word[j]==word[j+1]:
                    count+=1
                j+=1
            i=j
        return count
            


        