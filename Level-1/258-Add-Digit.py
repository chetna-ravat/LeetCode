class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        sum = 0
        while num > 0:
            x = num % 10
            sum += x
            num = num //10

        return self.addDigits(sum)

s = Solution()
assert 2 == s.addDigits(38)
assert 0 == s.addDigits(0)