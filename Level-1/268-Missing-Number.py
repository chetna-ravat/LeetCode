class Solution:
    def missingNumber(self, nums) -> int:
#         n = len(nums)
#         nums.sort()
#         for i in range(0,n):
#             if i != nums[i]:
#                 return i
#         return n
    
#     Alternatively
        n = len(nums)
        sum = 0
        value =  (n*(n+1))//2
        for i in nums:
            sum += i 

        ans = value - sum
        return ans

s = Solution()
assert 2 == s.missingNumber([3,0,1])
assert 2 == s.missingNumber([0,1])
assert 8 == s.missingNumber([9,6,4,2,3,5,7,0,1])