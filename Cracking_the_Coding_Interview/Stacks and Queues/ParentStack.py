class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.stack_size = stack_size
        self.array = [0] * stack_size * number_of_stacks
        self.sizes = [0] * self.number_of_stacks # Current size of each stack

    def _assert_valid_stack_num(self, stack_num): # Checks if input stack exists
        if stack_num >= self.number_of_stacks:
            raise ValueError(f'Stack #{stack_num} does not exist')
    
    def is_full(self, stack_num): # Returns True if input stack is at capacity
        return self.sizes[stack_num] == self.stack_size
    
    def is_empty(self, stack_num): # Returns True if input stack is empty
        return self.sizes[stack_num] == 0
    
    def index_of_top(self, stack_num): # Returns the index of the top of input stack, top of stack being on the right
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, value, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_full(stack_num):
            raise StackFullError(f'Push failed: stack #{stack_num} is full')
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value
        
    def pop(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f'Pop failed: stack #{stack_num} is empty')
        value = self.array[self.index_of_top(stack_num)]
        self.sizes[stack_num] -= 1
        self.array[self.index_of_top(stack_num)] = 0
        return value
    
    def peek(self, stack_num):
        self._assert_valid_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError(f'Peek failed: stack #{stack_num} is empty')
        return self.array[self.index_of_top(stack_num)]
    
class MultiStackError(Exception):
    """multistack operation error"""
    

class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""