
class Solution:
    def leftRigthDifference(self, nums):
        
        answer =[0] * len(nums)
        
        for i in range (1, len(nums)):
            answer[i] = answer[i-1] + nums[i-1]
        
        sum = 0   
        for j in range (len(nums) - 1, -1,-1):
            answer[j] = abs(answer[j] - sum)
            sum = sum + nums[j]
        
        return answer


nums = [10,4,11,6]
nums = [0]
nums = [10,15]
output = Solution()
assert True == output.leftRigthDifference(nums)