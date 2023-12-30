"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

"""
class MinStack:
    def __init__(self):
        self.items = []
        self.minvals = []

    def push(self, data):
        self.items.append(data)
        if len(self.minvals) == 0:
            self.minvals.append(data)
        elif data <= self.minvals[-1]:
            self.minvals.append(data)

    def pop(self):
        pop_value = self.items.pop()
        if self.minvals[-1] == pop_value:
            self.minvals.pop()
        return pop_value
    
    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def getMin(self):
        if len(self.minvals) == 0:
            return None
        return self.minvals[-1]


