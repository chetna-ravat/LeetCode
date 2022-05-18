from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        z = Counter(s)
        
        index = -1
        for i in s:
            index +=1
            if z[i] == 1:
                return index
       
        return -1

s = Solution()
assert 0 == s.firstUniqChar("leetcode")
assert 2 == s.firstUniqChar("loveleetcode")
assert -1 == s.firstUniqChar("aabb")
