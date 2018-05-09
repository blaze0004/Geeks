# Find length of a linkedlist (iterative and recursive method)

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
        
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        newnode.next = self.head
        self.head = newnode

    def iterativeLenghtCount(self):

        count = 0

        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count
    
    def recursiveLenghtCount(self, node):

        if node is None:
            return 0
        else:
            return 1 + self.recursiveLenghtCount(node.next)
        
if __name__ == "__main__":

    llist = LinkedList()
    for i in range(10,0, -1):
        llist.push(i)
    itrLength = llist.iterativeLenghtCount()
    recLenght = llist.recursiveLenghtCount(llist.head)

    print("Iterative Length is : {}\nRecursive Lenght is : {}".format(itrLength, recLenght))