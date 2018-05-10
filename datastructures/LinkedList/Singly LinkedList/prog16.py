# To check whether a linkedlist is palindrome or not 

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
        

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
            return

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def usingStack(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.next
        temp = self.head
        while temp:
            if stack.pop() is not temp.data:
                return False
            temp = temp.next
        del stack
        return True
    
    def tailRecReverse(self, node, prev):
        
        if node.next is None:
            self.head = node
            node.next = prev
            return 
            
        next = node.next
        node.next = prev

        self.tailRecReverse(next, node)


    def byReversing(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rotatedHalf = self.tailRecReverse(slow, None)
        temp = self.head
        tempRotate = rotatedHalf
        while rotatedHalf and temp:
            if temp.data != rotatedHalf.data:
                return False
            temp = temp.next    
            rotatedHalf = rotatedHalf.next
        self.tailRecReverse(tempRotate , slow)
        return True

    def usingRecursion(self):
        pass

# driver program

llist = LinkedList()
palinstr = input("Enter the string to check for palindrome: ")

for i in palinstr[::-1]:
    llist.push(i)
print(llist.printList())    

if llist.usingStack():
    print("Yes")
else:
    print("No")

if llist.byReversing():
    print("Yes")
else:
    print("No")

print(llist.printList())