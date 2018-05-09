# Find a element in linkedlist using iterative and recursive method

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
        print("Linkedlist is:")
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
        
    def iterativeSearch(self, key):

        if self.head is None:
            return False
        temp = self.head

        while temp:
            if temp.data is key:
                return True
            temp = temp.next
        
        return False

    def recursiveSearch(self, node, key):
        
        if node.next is None:
            return False
        if node.data is key:
            return True
        else:
            return self.recursiveSearch(node.next, key)
        
if __name__ == "__main__":
    llist = LinkedList()

    for i in range(10,0, -1):
        llist.push(i)
    
    print("Using Iterative Search:")
    print("Find 3")
    if llist.iterativeSearch(3):
        print("3 is in the Linkedlist")
    else:
        print("Not Found")
    print("Find 11")
    if llist.iterativeSearch(11):
        print("11 is in the Linkedlist")
    else:
        print("Not Found")    
        
    print("Using Recursive Search:")
    print("Find 3")
    if llist.recursiveSearch(llist.head, 3):
        print("3 is in the Linkedlist")
    else:
        print("Not Found")
    print("Find 11")
    if llist.recursiveSearch(llist.head, 11):
        print("11 is in the Linkedlist")
    else:
        print("Not Found")