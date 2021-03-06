# Deleting a linkedlist 


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

    def deleteLinkedList(self):
       # initialize the current node
        current = self.head
        while current:
            prev = current.next # move next node
             
            # delete the current node
            del current.data
             
            # set current equals prev node
            current = prev 

if __name__ == "__main__":
    llist = LinkedList()

    for i in range(19,3, -1):
        llist.push(i)

    llist.printList()

    llist.deleteLinkedList()

    llist.printList()