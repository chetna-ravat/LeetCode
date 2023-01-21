
# The variables(attributes) defined under constructer are accessible to all the functions(methods) in the class. 
# we access them using self.


class Node():
    def __init__(self, data, next= None):
        self.data = data
        self.next = next
        

class Linkedlist():
    def __init__(self):
        self.head = None
    
    # value argument in below function is not accessed by self. since it is simply used in the func below and will not be accessible outside this func 

    def append(self, value):
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


    def print(self):

        if self.head == None:
            return

        curr = self.head
        while curr != None:
            print(curr.data, " --> ", end ="")
            curr = curr.next
        print("None")


    def delete(self):
        if self.head == None:
            return
        
        prev = None
        curr = self.head

        # Our breaking condition below is on the last Node i.e. at last.next and not at None

        while curr.next != None:
            prev = curr
            curr = curr.next
    
        if prev == None:
            self.head = None
        else:
            prev.next = None

    def printRecurse(self):
        self.printrecursive(self.head)

    def printrecursive(self, curr):
        if curr == None:
            return
        else:
            print(curr.data)
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
result.append(7)
result.append(10)
result.append(18)
result.append(12)
result.printRecurse()
# result.printrecursive()








    
