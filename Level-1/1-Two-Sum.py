from typing import List
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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = list()
        for i in range (0, len(nums)):
            l.append((nums[i], i))

    #   Using Bubble sort algorithm to sort the array 

        for k in range (1, len(l)):
            for j in range (0, len(l)- k):
                if l[j][0]> l[j+1][0]:
                    swap = l[j]
                    l[j] = l[j+1]
                    l[j+1] = swap
        st = 0
        end = len(l)-1
        while st < end :
            if l[st][0] + l[end][0] == target:
                return l[st][1], l[end][1]
            
            elif l[st][0] + l[end][0] > target:
                end -= 1
                
            elif l[st][0] + l[end][0] < target:
                st += 1


s = Solution()
assert [0,1] == s.twoSum([2,7,11,15], 9)
assert [1,2] == s.twoSum([3,2,4], 6)
