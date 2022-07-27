from typing import List
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = max(nums)
        i = nums.index(w)
        nums[i]= 0
        
        x = max(nums)
        
        nums[i]= w
        
        y = min(nums)
        j = nums.index(y)
        nums[j] = w
        
        z = min(nums)
        
        nums[j] = y
        
        print(w,x,y,z)
        output = (w*x)-(y*z)
        
        return output

s = Solution()
assert 34 == s.maxProductDifference([5,6,2,7,4])
assert 64 == s.maxProductDifference([4,2,5,9,7,4,8])