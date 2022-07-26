class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
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

s = Solution()
assert True == s.containsNearbyDuplicate([1,2,3,1], 3)
assert False == s.containsNearbyDuplicate([1,2,3,1,2,3], 2)
assert True == s.containsNearbyDuplicate([1,0,1,1], 1)