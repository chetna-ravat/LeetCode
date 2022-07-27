class Solution:
    def countSegments(self, s: str) -> int:
        return self.efficientsolution(s)
    
    
    def efficientsolution(self, s):
        sum = 0
        for i in range(0, len(s)):
            if s[i]!= " " and (i == 0 or s[i-1]== " "):
                sum +=1
        return sum
        
    
    
    
    def mysolution(self, s):    
        i = 0
        count = 0
        
        while i < len(s):
            switch = False
            while i < len(s) and s[i] != " ":
                i +=1
                switch = True
            
            while i < len(s) and s[i] == " ":
                i +=1
            
            if switch == True:
                count +=1
                
        return count

s = Solution()
assert 5 == s.countSegments("Hello, my name is John")
assert 1 == s.countSegments("Hello")