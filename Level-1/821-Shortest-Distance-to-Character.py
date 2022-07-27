class Solution:
    def shortestToChar(self, s: str, c: str):
        l = list()
        i = 0
        while i < len(s) and s[i] != c:
            i +=1
            l.append(len(s))
            
        while i < len(s):
            if s[i] == c:
                index = 0
            else:
                index +=1
            l.append(index)
            i+=1
            
        i = len(s) - 1
        while i > 0 and s[i] != c:
            i -= 1
        
        while i >= 0:
            if s[i] == c:
                index = 0
            else:
                index +=1
                
            # l[i] = min(l[i], index)
            if l[i] > index:
                l[i] = index
            i-=1
        return l
                
                
                
s = Solution()
assert [3,2,1,0,1,0,0,1,2,2,1,0] == s.shortestToChar("loveleetcode", "e")
assert [3,2,1,0] == s.shortestToChar("aaab", "b")