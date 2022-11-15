
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # return self.inefficient(arr)
        return self.efficient(arr)
    
    def inefficient(self, arr):
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        return arr
        
    def efficient(self, arr):
        n = len(arr)
        
        # whatever the last element is would be max so far when we start from right
        max_ele = -1
        
        for i in range(n-1,-1,-1):
            curr_ele = arr[i]
            arr[i] = max_ele
            max_ele = max(curr_ele, max_ele)
            # if curr_ele > max_ele:
            #     max_ele = curr_ele
        return arr


# *************** Test Case *********************** 

result = Solution()
arr = [17,18,5,4,6,1]
output = result.efficient(arr)
assert [18,6,6,6,1,-1] == output

result = Solution()
arr = [17,18,5,4,6,1,19]
output = result.efficient(arr)
assert [19,19,19,19,19,19,-1] == output
