class Solution:
    def searchInsert(self, nums, target: int) -> int:
        ans = len(nums)
        l = 0
        r = len(nums)-1
        m = (l+r)//2
        
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                ans = m
                return ans
            elif target > nums[m]:
                l = m +1
            elif target < nums[m]:
                ans = m
                r = m - 1
                
        return ans

s = Solution()
assert 2 == s.searchInsert([1,3,5,6], 5)
assert 1 == s.searchInsert([1,3,5,6], 2)
assert 4 == s.searchInsert([1,3,5,6], 7)
assert 0 == s.searchInsert([1,3,5,6], 0)          
        