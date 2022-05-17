class Solution:
    def isValid(self, x: str) -> bool:
        open = ['[','{','(']
        mylist = list()
        close = {')':'(','}':'{',']':'['}
        for i in range(0,len(x)):
            if x[i] in open:
                mylist.append(x[i])
                
            elif len(mylist) !=0 and close[x[i]] == mylist[len(mylist)-1]:
                mylist.pop()
                
            else:
                return False
        if len(mylist) !=0:
            return False
        else:
            return True


s = Solution()
assert True == s.isValid("()")
assert True == s.isValid("()[]{}")
assert False == s.isValid("(([])")
