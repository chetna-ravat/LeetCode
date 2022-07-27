from collections import Counter
from typing import List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c = Counter(target)
        for i in arr:
            if i not in c :
                return False
            else: 
                c[i] -=1
                if c[i] < 0:
                    return False
        for i in range(0,len(c)):
            if c[i] >0 :
                return False
        
        for i in range(0, len(target)):        
            arr[i]= target[i]    
            
        return True

s = Solution()
assert True == s.canBeEqual([1,2,3,4], [2,4,1,3])
assert True == s.canBeEqual([7], [7])
assert False == s.canBeEqual([3,7,9], [3,7,11])