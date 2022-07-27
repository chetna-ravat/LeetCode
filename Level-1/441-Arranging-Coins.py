class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i =1
        # if n == 1:
        #     return 1
        
        while n >0 and (n-i) >=0:
            n -=i
            count +=1
            i +=1
        return count

s = Solution()
assert 2 == s.arrangeCoins(5)
assert 3 == s.arrangeCoins(8)