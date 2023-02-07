
# The variables defined under constructer are accessible to all the func(methods)in the class. 
# we access them using self.


class Node():
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
        

class Linkedlist():
    def __init__(self):
        self.head = None


    def insert(self, value, index):
        '''
        Inserting before first Node
        Inserting after any given Node
        '''
        
        if index < 0:
            raise "invalid index parameter"

        n1 = Node(value)
        if self.head == None:
            self.head = n1
        elif index == 0 and self.head != None:
            n1.next = self.head
            self.head = n1
        else:     
            n = 1
            curr = self.head
            while curr.next != None and n < index:
                curr = curr.next
                n += 1
            n1.next = curr.next
            curr.next = n1
    
    def insertAtEnd(self, value):
        curr = self.head
        prev = None

        # Our breaking condition below is after the last Node i.e. at None
        while curr != None :
            prev = curr
            # below is similar to i = i+1
            curr = curr.next
        
        node1 = Node(value)
        if self.head == None:
            self.head= node1
        else:
            prev.next = node1

    def insertInSortedList(self,value):
        '''
        **This function would only work in a sorted list**
        Cases considered: 
        Linkedlist is empty
        Duplicate values 
        '''
        
        n1 = Node(value)
        if self.head == None:
            self.head = n1
        else:
            curr = self.head
            prev = None
            while curr != None and curr.data < value:
                prev = curr
                curr = curr.next
            
            if prev == None:
                n1.next = self.head
                self.head = n1
            else:
                n1.next = prev.next
                prev.next = n1
        
    def delete(self,pos):

        '''
        This function deletes a given position/Node
        '''

        if self.head == None:
            return
        
        curr = self.head
        n = 1
        prev = None
        while curr != None and n < pos:
            prev = curr
            curr = curr.next
            n+=1
     
        # below condition checks if the given position is out of range 
        if curr == None:
            return
        # below condition is for deleting the first node 
        elif prev == None:
            self.head = curr.next
        else:
            prev.next = curr.next

    def deleteAtEnd(self):
        if self.head == None:
            return
        
        prev = None
        curr = self.head
        while curr.next != None:
            prev = curr
            curr = curr.next
        # below condition deltes the last remaining node
        if prev == None:
            self.head = None
        else:
            prev.next = None

    def reverseLinkedList(self):
        p = None
        q = None
        r = self.head
        while r != None:
            p = q
            q = r
            r = r.next
            q.next = p
        self.head = q
        return self.head

    def print(self):

        if self.head == None:
            return

        curr = self.head
        while curr != None:
            print(curr.data, " --> ", end ="")
            curr = curr.next
        print("None")


    def printRecurse(self):
        self.printrecursive(self.head)
        print("None")

    def printrecursive(self, curr):
        if curr == None:
            return 
        else:
            print(curr.data, "->", end = " ")
            self.printrecursive(curr.next)
        
    # def printrecursive(self, curr= Node(-1)):                   

    #     # (I am assuming that no Node will have a value of -1, 
    #     # then only this logic works.This is only for the first fun call)
    #     if curr != None and curr.data == -1:  
    #         curr = self.head
    #     if curr == None:
    #         print("None")
    #         return
    #     else:
    #         print(curr.data, " -> ", end = "")
    #         self.printrecursive(curr.next)




result = Linkedlist()
result.insert(10,0)
result.insert(15,3)
result.insertAtEnd(23)
result.insertInSortedList(50)
result.printRecurse()
x = result.reverseLinkedList()

result.printRecurse()
# result.printrecursive()








    
