# Deletion From A Given Position

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
        print("LinkedList is: ")
        temp = self.head 
        while temp:
            print(temp.data, end  = " ")
            temp = temp.next 

        print()

    def push(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def deletionNodeAt(self, position):
        print("Deletion At Position {}".format(position))
        if self.head is None:
            print("LinkedList is Empty")
            return
        
        temp = self.head

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return
        
        temp.next = temp.next.next

if __name__ == "__main__":

    llist = LinkedList()
    for i in range(6,0,-1):
        llist.push(i)
        llist.printList()

    
    llist.deletionNodeAt(4)
    llist.printList()