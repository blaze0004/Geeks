# Merging two sorted LinkedList

# 3 Methods
# 1. Using Dummy Node, 2. Using Local Reference, 3. Using Recursion

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList Class
class LinkedList:
    
    def __init__(self):
        self.head = None

    def printList(self):
        print("LinkedList is:")
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

        print()
        temp = None

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
            return

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

def usingDummyNode(a, b):
    dummy = Node(None)  
    tail = dummy
    while True:
        if a == None:
            dummy.next = b
            break
        elif b == None:
            dummy.next = a
            break
        if a.data <= b.data:
            # put data of a on dummy linkedlist
            dummy.next = Node(a.data)
            #print(dummy.next.data)
            a = a.next
            
        elif b.data <= a.data:
            dummy.next = Node(b.data)
            #print(dummy.next.data)
            b = b.next
            
        dummy = dummy.next
    return tail.next

def usingLocalReference():
    pass

def usingRecursion(a, b):
    result = Node(None)

    if a is None:
        return b
    elif b is None:
        return a
    
    if a.data <= b.data:
        result = a
        result.next = usingRecursion(a.next, b)
    elif b.data <= a.data:
        result = b
        result.next = usingRecursion(a, b.next)

    return result
# Driver Program

llist1 = LinkedList()

llist2 = LinkedList()

for i in range(20, 0, -1):
    if i % 2 == 0:
        llist1.push(i)
    else:
        llist2.push(i)

llist1.printList()
llist2.printList()

mergedList = LinkedList()

mergedList.head = usingDummyNode(llist1.head, llist2.head)

mergedList.printList()


mergedList.head = usingRecursion(llist1.head, llist2.head)
mergedList.printList()