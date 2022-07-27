from collections import Counter
from typing import List
class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        x = max(nums)
        y = min(nums)
        
        if count[x] + count[y] >= len(nums):
            return 0
        else:
            return (len(nums) - count[x]- count[y])

s = Solution()
assert 2 == s.countElements([11,7,2,15])
assert 2 == s.countElements([-3,3,3,90])   
        