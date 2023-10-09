"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there werejust a single stack).
FOLLOW UP
ImplementafunctionpopAt ( int index) which performs apopoperationon aspecificsub-stack.

SetOfStacks(self, number_of_stacks, capacity):
.push() - adds to current stack
.pop() - remove from current stack
.popAt() - remove at specific stack

Stack(self, capacity): 
.push()
.pop()
.is_full() - return if full
.is_empty() - return if empty

"""
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    
    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.items:
            print("Current stack data:", self.items)
            return self.items[-1]
        return None
    
    def is_full(self):
        return len(self.items) == self.capacity
    
    def is_empty(self):
        return len(self.items) == 0

    def print_all(self):
        if self.items:
            print('Stack data', self.items)
    

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def last_stack(self):
        if self.stacks:
            return self.stacks[-1]
        return None
    
    # Check if current stack is full
    # If full create new stack and add data
    # If not add data to current stack
    def push(self, data):
        last_stack = self.last_stack()
        if last_stack and not last_stack.is_full():
            last_stack.push(data)
        else:
            new_stack = Stack(self.capacity)
            new_stack.push(data)
            self.stacks.append(new_stack)

    # Ensure current stack is not empty
    # Perform pop on stack
    # If stack is empty then delete stack
    def pop(self):
        last_stack = self.last_stack()
        if last_stack and not last_stack.is_empty():
            pop = last_stack.pop()
            # print('Pop value:', pop)
            if last_stack.is_empty():
                del self.stacks[-1]
        else:
            return None

    # Stack.pop() at specified index
    # If Stack is not last in self.stacks 
    # Then go to the next stack and take the first index and push it to the previous stack
    # Repeat until you hit the last index 
    def popAt(self, index):
        index = index
        index_stack = self.stacks[index]
        pop_value = index_stack.pop()
        # print('Pop value:', pop_value)
        while index < len(self.stacks)-1:
            shift_var = self.stacks[index+1].items[0]
            index_stack.push(shift_var)
            del self.stacks[index+1].items[0]
            index += 1
            index_stack = self.stacks[index]
            
    def peek(self):
        last_stack = self.last_stack()
        if last_stack and not last_stack.is_empty():
            return last_stack.peek()
        else:
            return None
        
    def print_stacks(self):
        for stack in self.stacks:
            stack.print_all()
        

# Testing

plates = SetOfStacks(5)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.push(6)
plates.push(7)
plates.push(8)
plates.push(9)
plates.pop()
plates.push(10)
plates.push(11)
plates.push(12)
plates.push(13)
plates.push(14)
plates.push(15)
plates.push(16)
plates.print_stacks()
plates.popAt(2)
plates.print_stacks()