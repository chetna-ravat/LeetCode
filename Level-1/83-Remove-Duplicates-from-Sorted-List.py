
from multiprocessing.sharedctypes import Value


class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next 

class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        
        p = head.next
        q = head
        while p != None:
            if p.val == q.val:
                q.next = p.next
            else:
                q = p
            p = p.next 
        return head


# *************** Test Case *********************** 
result = Solution()
head = [1,1,2]
ans =  result.deleteDuplicates(head)
assert [1,2] == ans