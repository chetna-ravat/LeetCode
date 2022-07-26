class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        highest = 0
        for i in s:
            if i == "(":
                depth +=1
                # if depth > highest:
                #     highest = depth
            elif i == ")":
                depth -=1
            else:
                pass
            if depth > highest:
                highest = depth    
        return highest

#################  Test Case ##############

s = "(1+(2*3)+((8)/4))+1"  
t = Solution()
assert 3 == t.maxDepth(s)

s = "(1)+((2))+(((3)))"
t = Solution()
assert 3 == t.maxDepth(s)
