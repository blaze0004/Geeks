# Insertion In A Doubly LinkedList

# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly LinkedList Class

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        return

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode
        newnode.prev = temp
        return

    def insertAfter(self, node, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        temp = self.head

        while temp is not None:
            if temp == node:
                break
            temp = temp.next    
        
        if temp is None:
            return 
        newnode.next = temp.next
        temp.next.prev = newnode
        newnode.prev = temp
        temp.next = newnode
        return
        

    def insertBefore(self, node, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head 
        while temp is not None:
            if temp is node:
                break
            temp = temp.next

        if temp is None:
            return
        
        newnode.next = temp.prev.next 
        newnode.prev = temp.prev
        temp.prev.next = newnode
        temp.prev = newnode
        return

    def printList(self):
        
        temp = self.head

        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next

        print()

dll = DoublyLinkedList()

dll.push(1)

dll.append(4)
dll.insertBefore(dll.head.next, 3)
dll.insertAfter(dll.head, 2)

dll.printList()

