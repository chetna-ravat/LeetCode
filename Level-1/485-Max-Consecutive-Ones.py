from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        value = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count = 0
            if value < count :
                value = count 
        return value


# *************** Test Case *********************** 

result = Solution()
nums = [1,1,0,0,0,1,1,1]
ans =  result.findMaxConsecutiveOnes(nums)
assert 3 == ans


nums = [1,0,0,1,1,0,1]
ans =  result.findMaxConsecutiveOnes(nums)
assert 2 == ans