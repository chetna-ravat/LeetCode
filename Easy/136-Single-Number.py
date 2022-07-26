class Solution:
    def singleNumber(self, nums) -> int:
        # nums.sort()
        
        
        # for i in range (0,len(nums),2):
        #     if i!= len(nums)-1 and nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[len(nums)-1]
    
        # there is one more way to solve it , figure out later
        value = 0
        for i in nums:
            value = value^i  # XOR property x ^ x = 0 & x ^ 0 = x
        return value

s = Solution()
assert 1 == s.singleNumber([2, 2, 1])
assert 4 == s.singleNumber([4,1,2,1,2])
assert 1 == s.singleNumber([1])