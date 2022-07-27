class Solution:
    def peakIndexInMountainArray(self, nums) -> int:
        l = 0
        r = len(nums) -1
        ans = 0
        while l <=r:
            m = (l+r)//2
            if nums[m] > ans:
                value = m
                ans = max(ans,nums[m])
            if nums[m] < nums[m+1]:
                l = m +1
            elif nums[m] > nums[m+1]:
                r = m-1
        return value

s = Solution()
assert 1 == s.peakIndexInMountainArray([0,1,0])
assert 1 == s.peakIndexInMountainArray([0,2,1,0])
assert 1 == s.peakIndexInMountainArray([0,10,5,2])