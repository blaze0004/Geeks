# Node Class
class Node:
     # Function to initialize the node object 
     def __init__(self, data):
         self.data = data
         self.next = None

# Linked List Class
class LinkedList:

    #Function to initialize the LinkedList Object

    def __init__(self):
        self.head = None

    # Function For Traversal of LinkedList

    def printList(self):
        temp = self.head 
        print("LinkedList is: ")
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print()
if __name__ == '__main__':
    
    llist = LinkedList()

    llist.head = Node(1)

    second = Node(2)

    third = Node(3)

    llist.head.next = second;

    second.next = third;

    llist.printList()
    llist.printList()

