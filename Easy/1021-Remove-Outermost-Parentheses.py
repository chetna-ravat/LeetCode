class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        start = 0
        S = set([start])
        count = 0
        
        while i < len(s):
            if s[i] == "(":
                count +=1
            else:
                count -=1
            if count == 0:
                last = i
                S.add(last)
                if last != len(s)-1:
                    start = last+1
                    S.add(start)
                
            i+=1
            
        output = list()
        for i in range (0,len(s)):
            if i not in S:
                output.append(s[i])
        
        return "".join(output) 

s = "(()())(())"
t = Solution()
assert "()()()" == t.removeOuterParentheses(s)

s = "(()())(())(()(()))"
assert "()()()()(())" == t.removeOuterParentheses(s)