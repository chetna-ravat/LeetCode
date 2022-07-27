from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def swap(l,i,j):
            swap = l[i]
            l[i] = l[j]
            l[j] = swap
        
        
        b = Counter(nums)
        l = list()
        
        for key, value in b.items():
            l.append([key,value])
        print(l)
        for i in range(0, len(l)):
            for j in range (i+1, len(l)):
                
                if l[i][1] > l[j][1]:
                    swap(l,i,j)
                    
                elif l[i][1]== l[j][1]:
                    if l[i][0]< l[j][0]:
                        swap(l,i,j)
                    
      
        output = list()
        for i in range(0, len(l)):
            k = 0
            while k < l[i][1]:
                output.append(l[i][0])
                k +=1
        
        return output
    
s = Solution()
assert [3,1,1,2,2,2] == s.frequencySort([1,1,2,2,2,3])
assert [1,3,3,2,2] == s.frequencySort([2,3,1,3,2])
assert [5,-1,4,4,-6,-6,1,1,1] == s.frequencySort([-1,1,-6,4,5,-6,1,4,1])