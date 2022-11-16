from collections import Counter
from typing import List

class Solution:
    def heightChecker(self, h: List[int]) -> int:
        
        return self.efficient(h)
        
        
        
    def bruteforce(self, h):
        newarr = list(h)

        count = 0
        h.sort()
        for i in range(0,len(h)):
            if newarr[i] != h[i]:
                count +=1
        return count


    def efficient(self, h):
    
        dt = Counter(h)
       
        sortarr = list()
        for i in range (0, 101):
            if i in dt:
                freq = dt[i]
                while freq > 0:
                    sortarr.append(i)
                    freq -=1
        # print(sortarr)
        
        count =0
        for i in range (0, len(h)):
            if h[i] != sortarr[i]:
                count +=1
        return count           



# *************** Test Case ***********************

result = Solution()
h = [1,1,4,2,1,3]
output = result.efficient(h)
assert 3 == output


result = Solution()
h = [5,1,2,3,4]
output = result.efficient(h)
assert 5 == output