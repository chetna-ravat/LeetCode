class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 0
        i = 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j +=1
            if j < len(nums):
                nums[i+1] = nums[j]
                i +=1
        value = i
        for k in range(i+1,len(nums)):
            nums.pop()

s = Solution()
nums = [1,1,2]
n = s.removeDuplicates(nums)
assert [1, 2] == nums[:n]
nums = [0,0,1,1,1,2,2,3,3,4]
n == s.removeDuplicates(nums)
assert [0,1,2,3,4] == nums[:n]
