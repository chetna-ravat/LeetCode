# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5 ,"X":10,"L": 50, "C": 100, "D":500, "M":1000 }
        
        i = 0
        n = len(s) -1
        sum = 0
        while i < n:
            if d[s[i]] >= d [s[i+1]]:
                sum += d [s[i]]
            else:
                sum -= d [s[i]]
          
            i +=1
        sum += d [s[n]]
        return sum

s = Solution()
assert 3 == s.romanToInt("III")
assert 58 == s.romanToInt("LVIII")
assert 1994 == s.romanToInt("MCMXCIV")
