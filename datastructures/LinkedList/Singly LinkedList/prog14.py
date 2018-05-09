# Finding Loop in a Linkedlist
# 3 Methods

# 1. Using HashTable, 2. Marking Node Visiting, 3. Floyd Cycle Detection (best)

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

    def isLoopHash(self):
        visited = set()
        
        temp = self.head
        
        while temp:
            
            if temp in visited:
                return True
            
            visited.add(temp)
            
            temp = temp.next
            
        return False
        
    def isLoopFloyd(self):
        
        slow = fast = self.head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
        
if __name__ == "__main__":
    
    llist = LinkedList()
    
    llist = LinkedList()

    llist.push(20)

    llist.push(4)

    llist.push(15)

    llist.push(10)

    # Create a loop for testing

    llist.head.next.next.next.next = llist.head
    
    print("Loop Found") if llist.isLoopFloyd() else print("No loop")

