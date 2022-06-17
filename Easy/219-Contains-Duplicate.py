from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range (0, len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             print(i,j)
        #             if abs(i-j) <= k:
        #                 return True
        # return False
        
        
        
        d = dict()
        for i in range(0, len(nums)):
            # if nums[i] not in d:
            #     d[nums[i]] = i
            # elif abs(d[nums[i]]- i) <= k:
            #     return True
            # else:
            #     d[nums[i]] = i
                
            # simplified way of writing above if conditions
            if nums[i] in d and abs(d[nums[i]]- i) <= k:
                return True
            d[nums[i]] = i
                
        return False

nums = [1,2,3,1,4]
k = 3
s = Solution()
s.containsNearbyDuplicate(nums,k)
assert True == True

nums = [1,2,3,1,2,3]
k = 2
s = Solution()
s.containsNearbyDuplicate(nums,k)
assert False == False