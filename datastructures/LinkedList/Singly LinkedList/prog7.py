# Program to swap to node of linkedlist without swapping data

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

    def swapNodes(self, x, y):

        temp = self.head
        
        prev_x_found = False
        prev_y_found = False
        
        prev_x = self.head
        prev_y = self.head
        
        if self.head.data is x:
            prev_x_found = True
        
        elif self.head.data is y:
            prev_y_found = True
        
        while temp:
            if prev_x_found == False:
                if temp.next.data is x:
                    prev_x_found = True
                    prev_x = temp
                    temp = temp.next
                    continue
            if prev_y_found == False:
                if temp.next.data is y:
                    prev_y_found = True
                    prev_y = temp
                    temp = temp.next
                    continue

            if prev_y_found == prev_x_found == True:
                break

            temp = temp.next
        prev_x.next, prev_y.next = prev_y.next, prev_x.next
        prev_x.next.next, prev_y.next.next = prev_y.next.next, prev_x.next.next

if __name__ == "__main__":
    llist = LinkedList()

    for i in range(10, 0, -1):
        llist.push(i)

    llist.printList()

    llist.swapNodes(4, 8)

    llist.printList()

