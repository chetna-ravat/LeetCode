
from typing import List
class Solution:
    def bubbleSort(self, nums: List[int]):
        n = len(nums)
        for k in range (1, n):
            for j in range (0, n- k):
                if nums[j]> nums[j+1]:
                    swap = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = swap
s = Solution()
nums = [2, 5, 3, 4, 1]
s.bubbleSort(nums)
assert [1, 2, 3, 4, 5] == nums

nums = [1, 1, 1]
s.bubbleSort(nums)
assert [1, 1, 1] == nums

nums = [1, -1, 0]
s.bubbleSort(nums)
assert [-1, 0, 1] == nums