# Deletion In A linkedList

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
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        temp = None
        print()


    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    # Deletion of a node

    def deleteNode(self, data):
        
        if self.head is None:
            print("LinkedList Is Empty")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next.data != data and temp:
            temp = temp.next
        
        if temp is None:
            print("Data is not present in LinkedList")
            return
        
        temp.next = temp.next.next

        temp = None


if __name__ == "__main__":
     
     llist = LinkedList()
     llist.push(5)
     llist.push(4)
     llist.push(3)
     llist.push(2)
     llist.push(1)
     llist.push(0)

     llist.printList()

     llist.deleteNode(3)

     llist.printList()
        

