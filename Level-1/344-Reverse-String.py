class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = 0
        n = len(s)-1
        while x < n:
            store = s[x]
            s[x] = s[n]
            s[n]= store
            x +=1
            n -=1


s = Solution()
st = ["h","e","l","l","o"]
s.reverseString(st)
assert ["o","l","l","e","h"] == st

st = ["H","a","n","n","a","h"]
s.reverseString(st)
assert ["h","a","n","n","a","H"] == st