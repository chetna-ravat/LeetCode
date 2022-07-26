class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        return self.efficient(nums, target)
    
    
    
    def usingForLoop(self, nums, target):
        n = len(nums)-1
        for i in range (0, n):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j] == target:
                    return i,j 
    
    
    def usingdict(self,nums, target):
        d = dict()
        l = list()
        for i in range (0, len(nums)):
            d[nums[i]] = i
        for i in range (0, len(nums)):
            z = target - nums[i]
            if z in d and d[z] != i:
                l.append(i)
                l.append(d[z])
                return l
                
                
    def efficient(self, nums, target):
        d = dict()
        for i in range(0, len(nums)):
            value = target - nums[i] 
            if value in d:
                return i, d[value]
            else:
                d[nums[i]] = i


s = Solution()
assert [0,1] == s.twoSum([2,7,11,15], 9)
assert [1,2] == s.twoSum([3,2,4], 6)
