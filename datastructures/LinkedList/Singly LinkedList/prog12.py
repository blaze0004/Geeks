# Count a given number occurence in a linkedlist


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

    def countGivenNumber(self, key):
        count = 0
        temp = self.head
        while temp:
            if temp.data is key:
                count += 1

            temp = temp.next
        return count

if __name__ == "__main__":
    llist = LinkedList()

    for i in range(10,2,-1):
        llist.push(i)
        if i % 2 == 0:
            llist.push(i)
            llist.push(i)

    llist.printList()

    print(llist.countGivenNumber(4))