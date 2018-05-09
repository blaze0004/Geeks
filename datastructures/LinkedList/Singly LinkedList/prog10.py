# Print the nth node from the end in Linkedlist
# 2 Method
# 1. Use Length of the linkedlist 
# 2. Use two pointers


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

    def useLenght(self, position):
        print("Printing {} element from the end".format(position))
        lenght = 0

        temp = self.head

        while temp:
            lenght += 1
            temp = temp.next

        if lenght < position:
            return 

        temp = self.head
        
        for i in range(lenght-position):
            temp = temp.next
        
        return temp.data


    def useTwoPointers(self, position):
        print("Printing {} element from the end".format(position))
        ptr1 = ptr2 = self.head

        for i in range(position):
            ptr1 = ptr1.next

        while ptr1:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        return ptr2.data

if __name__ == "__main__":
    llist = LinkedList()

    for i in range(20, 0, -1):
        llist.push(i)
    
    llist.printList()

    print("Using Method 1 (Using Length): {}".format(llist.useLenght(3)))
    print("Using Method 2 (Using 2 pointers): {}".format(llist.useTwoPointers(3)))
