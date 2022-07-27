from collections import Counter 

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return self.myoriginalsolution(s,t)
        
        
    def myoriginalsolution(self,s,t):
        d = Counter(t)
        for i in s:
            d[i] -=1
        for k,v in d.items():
            if v > 0:
                return k

s = Solution()

assert "e" == s.findTheDifference("abcd", "abcde")
assert "y" == s.findTheDifference("", "y")