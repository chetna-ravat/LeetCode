class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = list()
        top = len(st) - 1
        
        for i in range (0, len(s)):
            if len(st) > 0 and st[top] == s[i]:
                st.pop()
            else:
                st.append(s[i])
            top = len(st) - 1
        
        output = "".join(st)
        return output

s = Solution()

assert "ca" == s.removeDuplicates("abbaca")
assert "ay" == s.removeDuplicates("azxxzy")
