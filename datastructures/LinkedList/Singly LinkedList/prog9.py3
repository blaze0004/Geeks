# Find Middle of linkedlist 
# 3 Methods

# 1. Traverse Whole, 2. Use Two Pointers.
# 3. Initialize mid as head

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

    def findMiddleTraverseWhole(self):
        count = 0
        temp = self.head 

        while temp:
            count += 1
            temp = temp.next
        
        temp = self.head
        for i in range(count//2):
            temp = temp.next

        return temp.data

    def findMiddleUsingTwoPointers(self):
        ptr1 = ptr2 = self.head

        while ptr1 and ptr1.next:
            ptr2 = ptr2.next
        
            ptr1 = ptr1.next.next
        
        return ptr2.data
    
    def findMiddleByInitializeAsHead(self):
        mid = self.head

        temp = self.head
        count = 0
        while temp:
            if count%2 != 0:
                mid = mid.next
            temp = temp.next
            count += 1
        
        return mid.data

if __name__ == "__main__":

    llist1 = LinkedList()
    llist2 = LinkedList()

    for i in range(20, 0, -1):
        llist1.push(i)
        if i < 10:
            llist2.push(i)
    
    print('Linkedlist1 is:')
    llist1.printList()
    print("Linkedlist 2 is: ")
    llist2.printList()

    print("find Middle using method 1, 2, 3 respectively")

    print("For Linkedlist 1: ")
    print(llist1.findMiddleTraverseWhole())
    print(llist1.findMiddleUsingTwoPointers())
    print(llist1.findMiddleByInitializeAsHead())

    print("For Linkedlist 2: ")
    print(llist2.findMiddleTraverseWhole())
    print(llist2.findMiddleUsingTwoPointers())
    print(llist2.findMiddleByInitializeAsHead())
    