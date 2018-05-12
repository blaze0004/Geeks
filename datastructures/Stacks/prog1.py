# Implementation of stack using array and LinkedList

# Using Array 

# stackusingarray class

from sys import maxsize

class StackUsingArray:

    def __init__(self):
        self.stack = []
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, data):
        
        if self.top == maxsize:
            print("Stack overflow")
            return
        self.stack.append(data)
        self.top += 1

        print("{} is pushed on the stack".format(self.stack[self.top]))

    
    def pop(self):
        
        if self.isEmpty():
            print("Stack Underflow")
            return

        item = self.stack[-1]
        del self.stack[-1]
        self.top -= 1
        return item 

    def peek(self):
        return self.stack[self.top]

# Stack using linkedlist

# Node Class

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

# stack using linkedlist class

class StackUsingLL:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head is None else False

    def push(self, data):

        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        print("{} is pushed to stack".format(data))
        
    def pop(self):

        if self.isEmpty():
            print("Stack underflow")
            return
        
        item = self.head

        self.head = self.head.next
        return item.data

# Driver for stack using array class

stackArray = StackUsingArray()

for i in range(10):
    stackArray.push(i)

print(stackArray.top)
print(stackArray.peek())
print(stackArray.pop())



# Driver for stack using linkedlist class

stackLL = StackUsingLL()

for i in range(10):
    stackLL.push(i)

print("Top of the stack is {}".format(stackLL.head.data))

print(stackLL.pop())