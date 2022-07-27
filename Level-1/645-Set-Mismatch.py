class Solution:
    def findErrorNums(self, nums):
        
        sum = 0
        s= set()
        output = list()
        for i in range(0, len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
                sum += nums[i]
            else:
                output.append(nums[i])
        n = len(nums)
        ans = (n*(n+1))//2
        value = ans - sum
        output.append(value)
        return output

s = Solution()

assert [2,3] == s.findErrorNums([1,2,2,4])
assert [1,2] == s.findErrorNums([1,1])