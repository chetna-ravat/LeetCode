from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        switch = True
        while tickets[k] > 0 and switch == True:
            for i in range (0, len(tickets)):
                if tickets[k]== 0:
                    switch = False
                    break 
                if tickets[i] > 0:
                    z = tickets[i]
                    l = z - 1
                    tickets[i]= l
                    time +=1
        return time    

s = Solution()
assert 6 == s.timeRequiredToBuy([2,3,2], 2)
assert 8 == s.timeRequiredToBuy([5,1,1,1], 0)