"""
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted inascendingorder
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks

start
middle
end

TOH(n = 1, start, middle, end)
start -> end

TOH(n = 2, start, middle, end)
start -> middle 1
start -> end 2
middle -> end 1

TOH(n = 3, start, middle, end)
"start -> end 1
start -> middle 2
end -> middle 1" => TOH(n = 2, start, end, middle)

start -> end 3

"middle -> start 1
middle -> end 2
start -> end 1 " => TOH(n=2, middle, start, end)

TOH(n, start, middle, end) = 
-TOH(n-1, start, end, middle) -> moves disks on top of target base onto middle stack
-Move target base onto end
-TOH(n-1, middle, start, end) -> moves disks from middle stack to end stack

class Stack
    -holds disks
    -FILO, pop()
    -add

def TOH(n, start, middle, end)
-n = number of disks first stack begins with
-start = initial stack holding disks that need to be moved
-middle = stack used for buffer
-end = target stack for disks after transfer
"""

class Stack:
    def __init__(self):
        self.disks = []

    def pop(self):
        return self.disks.pop()
    
    def add(self, disk):
        return self.disks.append(disk)
    
    def start(self, n):
        for count in range(n, 0, -1):
            self.disks.append(count)

def TOH(n, start, middle, end):
    if n == 0:
        return

    TOH(n-1, start, end, middle)
    base = start.pop()
    if len(end.disks) >= 1:
        if base < end.disks[-1]:
            end.add(base)
        else:
            return ('Error!!!!')
    else:
        end.add(base)
    TOH(n-1, middle, start, end)


# Testing:
if __name__ == "__main__":
    start = Stack()
    start.start(10)
    middle = Stack()
    end = Stack()
    print(f'Start:{start.disks}')
    print(f'Middle:{middle.disks}')
    print(f'End:{end.disks}')
    TOH(10, start, middle, end)
    print(f'Start:{start.disks}')
    print(f'Middle:{middle.disks}')
    print(f'End:{end.disks}')




