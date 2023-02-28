def printIterative(head):
    if head == None:
        return

    curr = head
    while curr != None:
        print(curr.data, " --> ", end ="")
        curr = curr.next
    print("None")

def printRecursive(curr):
    if curr == None:
        return 
    else:
        print(curr.data, "->", end = " ")
        printRecursive(curr.next)

