class Solution:
    def isPowerOfThree(self, nums: int) -> bool:
        
        if nums == 0:
            return False
        return self.ispower(nums)
        
    def ispower(self, nums):
        if nums == 1:
            return True
        if nums % 3 == 0:
            nums = nums//3
            return self.ispower(nums)
             
        else:
            return False

################## Test Case ##########

s = Solution()
nums = 27
ans = s.isPowerOfThree(nums)
assert True == ans

nums = 15
ans = s.isPowerOfThree(nums)
assert False == ans

nums = 0
ans = s.isPowerOfThree(nums)
assert False == ans

nums = 1
ans = s.isPowerOfThree(nums)
assert True == ans
