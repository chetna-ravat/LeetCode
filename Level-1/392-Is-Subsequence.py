class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in s:
            while j < len(t) and t[j] != i:
                j+=1
            if j == len(t):
                return False
            j +=1
        return True


s = Solution()
assert True == s.isSubsequence("abc", "ahbgdc")
assert False == s.isSubsequence("axc", "ahbgdc")