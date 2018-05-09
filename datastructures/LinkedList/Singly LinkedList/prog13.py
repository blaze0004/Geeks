# Reverse a Linked List 
# 3 Method
# 1. Iterative , 2. Recursive, 3. Tail Recursion


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

    def iterativeReverse(self):
        prev = next = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
    
    def recReverse(self):
        pass

    def tailRecReverse(self):
        pass