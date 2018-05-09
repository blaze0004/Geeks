# function to get Nth node in a Linked List
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

    def getNth(self, position):
        temp = self.head

        for i in range(position):
            temp = temp.next
        
        if temp is None:
            return 
        return temp.data

if __name__ == "__main__":
    llist =  LinkedList()
    
    for i in range(10,0,-1):
        llist.push(i)
    
    llist.printList()
    
    print(llist.getNth(3))