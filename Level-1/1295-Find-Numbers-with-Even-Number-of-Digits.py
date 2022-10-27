from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
     
        output = 0
        for i in range(0, len(nums)):
            count  = 0
            while nums[i] > 0:
                nums[i] = nums[i]//10
                count +=1
            if count % 2 == 0:
                output +=1
        return output


# *************** Test Case *********************** 

result = Solution()
nums = [555,901,482,1771]
ans =  result.findNumbers(nums)
assert 1 == ans


nums = [12,345,2,6,7896]
ans =  result.findNumbers(nums)
assert 1 == ans

