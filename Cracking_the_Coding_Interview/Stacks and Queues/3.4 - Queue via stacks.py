"""
Implement a MyQueue class which implements a queue using two stacks.

Approach:
- We could just edit pop and peak as those 2 methods are the primary differences between stacks and queues
   but that's not what is intended.
- You have the intial stack that holds the numbers in order, push should remain the same
- When you want to pop, because pop works the same, the elements are going to need to be reversed pior to 
    returning the value

push_stack: [1,2,3,4,5,6,7]

- When push is called push_stack is used

pop_stack: [7,6,5,4,3,2,1]

- When pop/peek are called then pop_stack is used
- Pop/peek should apply to the first element that was added to the Queue aka the first element in the push_stack
- In order to reduce the amount of calls we can limit any transfers of data from push_stack to pop_stack
    to only when pop_stack is empty

Class myQueue
    class push_stack
    class pop_stack
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.items:
            # print('Stack elements:', self.items)
            # print('Stack peek:', self.items[-1])
            return self.items[-1]
        return None

class myQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    # Push adds elements to the end of push_stack
    def push(self, data):
        self.push_stack.push(data)
        # print('Push_stack items:', self.push_stack.items)

    # Pop removes elements from the end of pop_stack
    # If pop_stack is empty then pop elements from push_stack and push to pop_stack
    def pop(self):
        if len(self.pop_stack.items) == 0:
            while len(self.push_stack.items) > 0:
                element = self.push_stack.pop()
                self.pop_stack.push(element)
            # print('Pop_stack items w/ add:', self.pop_stack.items)
            return self.pop_stack.pop()
        else:
            # print('Pop_stack items no add:', self.pop_stack.items)
            return self.pop_stack.pop()
        

    # Peek should be the same as pop but instead of pop you perform peek
    def peek(self):
        # print('Pop_stack items:', self.pop_stack.items)
        if len(self.pop_stack.items) == 0:
            while len(self.push_stack.items) > 0:
                element = self.push_stack.pop()
                self.pop_stack.push(element)
            # print('Pop_stack items w/ add:', self.pop_stack.items)
            return self.pop_stack.peek()
        else:
            return self.pop_stack.peek()

# Testing:

queue = myQueue()

queue.push(1)
print('Peek (1):', queue.peek())
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
print('Peek (1):', queue.peek())
print('Pop queue:', queue.pop())
print('Peek (2):', queue.peek())
print('Pop queue:', queue.pop())
print('Pop queue:', queue.pop())
print('Pop queue:', queue.pop())
print('Peek:', queue.peek())



