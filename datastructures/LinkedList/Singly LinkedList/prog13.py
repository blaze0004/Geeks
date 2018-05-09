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
        
        current = self.head
        prev = None
        next = None

        while current:

            next = current.next
            current.next = prev
            prev, current = current, next 

        self.head = prev
        
    def recReverse(self, node):
    
        if node.next is None:
            self.head = node
            return
        
        self.recReverse(node.next)

        prev = node.next
        prev.next = node
        node.next = None

    def tailRecReverse(self, node, prev):
        
        if node.next is None:
            self.head = node
            node.next = prev
            return
        

        self.tailRecReverse(node.next, )


if __name__ == "__main__":
    
    llist = LinkedList()

    for i in range(10, 0, -1):
        llist.push(i)

    llist.printList()

    llist.iterativeReverse()

    llist.printList()

    llist.recReverse(llist.head)

    llist.printList()

    llist.tailRecReverse(llist.head, None)

    llist.printList()