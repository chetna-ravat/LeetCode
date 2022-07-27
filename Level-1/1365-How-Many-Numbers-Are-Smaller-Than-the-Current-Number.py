from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        l =list()
        for i in range(0, len(nums)):
            count= 0
            for j in range (0, len(nums)):
                if nums[j] < nums[i]:
                    count +=1
            l.append(count)
        
        return l

s = Solution()
assert [4,0,1,1,3] == s.smallerNumbersThanCurrent([8,1,2,2,3])
assert [2,1,0,3] == s.smallerNumbersThanCurrent([6,5,4,8])
assert [0,0,0,0] == s.smallerNumbersThanCurrent([7,7,7,7])