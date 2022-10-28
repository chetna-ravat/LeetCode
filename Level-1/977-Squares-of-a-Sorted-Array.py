from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i] **2
        
        return self.twopointer(nums)
         
    
    def twopointer(self,nums):
        n = len(nums)
        result = [0]*n
        l = 0
        r = n-1
        k = n-1
        while  l<= r:           
            if nums[l] > nums[r]:
                result[k] = nums[l]
                l +=1
            else:
                result[k] = nums[r]
                r -=1
            k -=1
        return result   
        
    
    
    def bubblesort(self,nums):
        for i in range(1, len(nums)):
            flag = False
            for j in range (0, len(nums) - i):
                if nums[j] > nums[j + 1]:
                    swap = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = swap
                    flag = True
            if flag == False:
                return nums
        return nums



# *************** Test Case *********************** 

result = Solution()
nums = [-4,-1,0,3,10]
ans =  result.sortedSquares(nums)
assert [0,1,9,16,100] == ans


nums = [-7,-3,2,3,11]
ans =  result.sortedSquares(nums)
assert [4,9,9,49,121] == ans