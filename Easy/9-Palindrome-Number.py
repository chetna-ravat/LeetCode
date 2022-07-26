class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        c = x
        l = list()
        value = 0
        if x < 0:
            return False
        
        
        while x > 0:
            y = x % 10
            l.append(y)
            x = x//10
        
        n = len(l) -1
        for i in l:
            value += (10**n) * i
            n -=1
        if value == c:
            return True
        return False

s = Solution()
assert True == s.isPalindrome(121)
assert False == s.isPalindrome(-121)
assert False == s.isPalindrome(10)