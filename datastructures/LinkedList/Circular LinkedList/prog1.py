
# Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular LinkedList Class
class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):

        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode
        
    def printList(self):

        if self.head is None:
            print("Empty")
            return
        temp = self.head

        print(temp.data, end = " ")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end = " ")
            temp = temp.next

        print()

cllist = CircularLinkedList()

for i in range(10, 0, -1):
    cllist.push(i)

cllist.printList()
