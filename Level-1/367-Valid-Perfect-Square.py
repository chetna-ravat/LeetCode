class Solution:
    def isPerfectSquare(self, num: int) -> bool:      
        l = 1
        r = num
        while l <= r :
            m = (l+r)//2
            if m**2 == num:
                return True
            elif m**2 > num:
                r = m-1
            elif m**2 < num :
                l = m+1
        
        if num == 1:
             return True        
        return False

############## Test Case #############
s = Solution()
num = 16
assert True == s.isPerfectSquare(num) 

num = 20678
assert False == s.isPerfectSquare(num) 

num = 1
assert True == s.isPerfectSquare(num)
