from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mostefficient(nums)
    
    def mostefficient(self, nums):
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index +=1
                
        for i in range(index, len(nums)):
            nums[i] = 0
             
    def usingWhilePointer(self, nums):
        
        i = 0
        
        while i < len(nums) and nums[i] !=0:
            i+=1   
        j = i+1    
        while j < len(nums) and nums[j] == 0:
            j +=1
        
        
        while j < len(nums):
            nums[i] = nums[j]
            nums[j] = 0
            while i < len(nums) and nums[i] !=0:
                i +=1
            while j < len(nums) and nums[j] == 0:
                j +=1
            
    def verylamesolution(self, nums):

        l = list()
        
        for i in range (0, len(nums)):
            if nums[i] == 0:
                l.append(i)
        
        n = len(l)
        for i in range (n-1, -1,-1):
            print(nums[l[i]])
            del(nums[l[i]])
        
        m = 0
        while m < n:
            nums.append(0)
            m +=1



############ Test Case ##############
efficient = Solution()

nums = [1,2,0,4,0,9,0,8]
efficient.mostefficient(nums)
assert [1,2,4,9,8,0,0,0] == nums

nums = [1,2,4,5,6]
efficient.mostefficient(nums)
assert [1,2,4,5,6] == nums

nums = [0,0,0,0]
efficient.mostefficient(nums)
assert [0,0,0,0] == nums

nums = [0,0,0,1]
efficient.mostefficient(nums)
assert [1,0,0,0] == nums