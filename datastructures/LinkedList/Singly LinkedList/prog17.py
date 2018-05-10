# Get the intersection point of two linkedlist

# 7 Methods

# 1. Simply Use two loops
# 2. Mark Visited Nodes
# 3. Using difference of node count
# 4. Make circle in first list
# 5. Reverse the linkedlist and make equations
# 6. Traverse both and match the addresses of last node
# 7. Use Hashing 

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

def useHashing(list1, list2):
    itrlist1 = list1
    itrlist2 = list2

    hashtable = set()

    while itrlist1:
        hashtable.add(itrlist1)
        itrlist1 = itrlist1.next
    
    while itrlist2:
        if itrlist2 in hashtable:
            return itrlist2
        itrlist2 = itrlist2.next

    return -1

llist1 = LinkedList()
llist2 = LinkedList()

for i in range(10, 0, -1):
    llist1.push(i)

for i in range(12, 20):
    llist2.push(i)

llist2.next = llist1

pointOfIntersectin = useHashing(llist1, llist2)
if pointOfIntersectin == -1:
    print("No Intersection")

else:
    print("intersection at node: {}".format(pointOfIntersectin.data))

