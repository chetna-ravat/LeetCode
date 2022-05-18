from collections import Counter
from collections import deque

class Solution:
    def countStudents(self, S, b) -> int:
    #s refers to students and b refers to burger/sandwiches   
       
        s = deque(S)
        b.reverse()
        n = len(b) - 1
        d = Counter(s)
        
        while n >=0 and d[b[n]] != 0:
            
            if s[0] == b[n]:
                d[s[0]] -=1
                b.pop()
                s.popleft()
            else:
                r = s.popleft()
                s.append(r)
            n = len(b) - 1
        return len(b)
    
                
                
s = Solution()
students = [1,1,0,0]
sandwiches = [0,1,0,1]
assert 0 == s.countStudents(students, sandwiches)

students = [1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
assert 3 == s.countStudents(students, sandwiches)
