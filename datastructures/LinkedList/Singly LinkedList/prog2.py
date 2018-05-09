# Program for insertion in a linkedlist

# Node Class

class Node:
    #function to initialize node object

    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList Class

class LinkedList:

    #function to initialize linkedlist object
    def __init__(self):
        self.head = None
        self.printList()
    #function to traverse linked list and print

    def printList(self):
        temp = self.head 
        print("LinkedList is: ")
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print()

    # Insertion At Beginning

    def push(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return 

        new_node.next = self.head

        self.head = new_node

        self.printList()

    # Insertion at end

    def append(self, data):
        
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp  = self.head

        while(temp.next):
            temp = temp.next

        temp.next = new_node

        self.printList()


    # insertion at a given location

    def insertAfter(self, prev_node, data):

        if prev_node is None:
            print("The given node must be in LinkedList")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        self.printList()

if __name__ == "__main__":

    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)

    llist.printList()



        