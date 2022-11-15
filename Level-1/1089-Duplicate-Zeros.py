from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        self.inplace_solution(arr)
        
    
                
    def inplace_solution(self,arr):
        i = k =0
        while k < len(arr):
            if arr[i] != 0:
                k +=1
            else: 
                k +=2
            i +=1

        i = i-1
        j = len(arr) -1
        if k > len(arr):
            arr[j] = arr[i]
            i-=1
            j -=1

        while i>=0:
            if arr[i] != 0:
                arr[j] = arr[i]
                j -=1
            else:
                arr[j] = arr[i]
                arr[j-1] = arr[i]
                j -=2
            i -=1

    def newarrary(self,arr):
        i = 0
        k = 0
        newarr = [0] * len(arr)
        while k < len(arr):
            if arr[i] != 0:
                newarr[k] = arr[i]
                k +=1
            elif arr[i] == 0:
                k +=2
            i +=1

        for i in range (0, len(arr)):
            arr[i] = newarr[i]



# *************** Test Case *********************** 

result = Solution()
nums = [1,0,2,3,0,4,5,0]
result.inplace_solution(nums)
assert [1,0,0,2,3,0,0,4] == nums


nums = [1,2,3,0,0,0,0,0]
result.inplace_solution(nums)
assert [1,2,3,0,0,0,0,0] == nums