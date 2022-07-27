class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] >  target: 
                r = m -1
            elif nums[m] <  target: 
                l = m +1
        return -1

s = Solution()
assert 4 == s.search([-1,0,3,5,9,12], 9)
assert -1 == s.search([-1,0,3,5,9,12], 2)