"""
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Thinking:
-Instead we can store the smallest value of each stack as values are add removed
-The smallest value is updated with each push or pop call
-This allows us to have the smallest value stored and when min is called we just return the value
-The problem with this is as you remove values you have to find the old minimum value again
-That problem can be solved by creating a linked list minvalue class acting as the node to point to the previous 
-   minium value

Approach:
-create minvalue class


"""

class Stack:
    def __init__(self):
        self.items = []
        self.minvals = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)
        if len(self.minvals) == 0:
            self.minvals.append(data)
        elif data <= self.minvals[-1]:
                self.minvals.append(data)

    def pop(self):
        if self.items[-1] == self.minvals:
            del self.minvals[-1]
        return self.items.pop()
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def minval(self):
        if self.minvals:
            return self.minvals[-1]
        return None

    def __len__(self):
        return len(self.items)
    
    def __bool__(self):
        return bool(self.items)
    
#testing

stack = Stack()

stack.push(5)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())
stack.push(6)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())
stack.push(3)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())
stack.push(7)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())
stack.push(8)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())
stack.push(1)
print('Peek:', stack.peek())
print('Min Value:', stack.minval())

