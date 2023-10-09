"""
Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array).The stack supports the following operations: push, pop, peek, and isEmpty.

Approach:
- Utilizing 2 stacks you can reverse main_stack into temp_stack
- If you find an element out of order the store it in a holding variable
- Continue to reverse the order until the holding variable can be placed in the correct spot

main_stack: [1,4,10,5,2] -> [1,4,10]   -> [1,4,10,2] -> [1,4] -> [1,2]  -> [1]        -> []          
temp_stack: []           -> [2]        -> [5]        -> [5,2] -> [10,5] -> [10,5,4,2] -> [10,5,4,2,1]
hold_var:   0            -> 5          -> 0          -> 10    -> 4      -> 0          -> 0           

- In order to accomplish this we must follow some basic rules
1.) The element getting pushed to temp_stack must be greater than the last element in temp_stack
2.) The last element in temp_stack must be greater than hold_var
    - If the temp_stack[-1] < pushing element:
        -move pushing element to hold_var
        -pop & push temp_stack[-1] to main_stack until hold_var is < temp_stack[-1]
        -push hold_var into temp_stack

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
            return self.items[-1]
        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
def sort_stack(stack):
    main_stack = stack
    temp_stack = Stack()
    hold_var = 0
    print('Main stack items:', main_stack.items)
    while len(main_stack.items) != 0:
        hold_var = main_stack.pop()
        # print('hold_var:', hold_var)
        if temp_stack.isEmpty():
            temp_stack.push(hold_var)
        else:
            while not temp_stack.isEmpty() and hold_var > temp_stack.peek():
                # print('Temp_stack:', temp_stack.items)
                main_stack.push(temp_stack.pop())
                # print('Main stack items after push:', main_stack.items)
            temp_stack.push(hold_var)
    print('Temp stack items:', temp_stack.items)
    return temp_stack.items

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(10)
    stack.push(0)
    stack.push(2)
    stack.push(0)
    sort_stack(stack)


    