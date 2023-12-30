"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

examples:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Notes:
-3 pointers: slow, middle, fast
-Slow = the node that we are weaving after
-Middle = node after slow pointer
-Fast = last node in the list
-Slow = L0, middle = L1, fast = Ln
-slow.next = fast
-fast.next = middle
-At this point we have reordered to L0 -> Ln -> L1 -> ...
-Move slow to middle then middle to slow.next and restart the process until slow.next == None

"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def print_llist(self):
        if self.head == None:
            return print('No Nodes')
        
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

def reorder_bruteforce(llist):
    # Initiate 3 pointers
    slow = llist.head
    middle = slow.next
    fast = llist.head
    end = llist.head

    # Continue reordering until slow reaches the end of the linked list
    while slow.next:
    
        # Move fast to the last node
        while fast.next.next:
            fast = fast.next

        if fast.next:
            end = fast
            fast = fast.next

        # Move the last node to after the slow pointer
        end.next = None
        slow.next = fast
        fast.next = middle
        slow = middle
        middle = slow.next

    # Printing the answer in a nicer format
    slow = llist.head
    answer = []

    while slow:
        answer.append(slow.data)
        slow = slow.next

    return print(answer)

def reorder_improved(llist):
    # Split the llist in half, first half is longer if odd number of nodes
    first, second = llist.head, llist.head.next
    while second and second.next:
        first = first.next
        second = second.next.next

    # Reverse 2nd list
    # Second is at the start of the 2nd list
    # Slow represents where we are going to move the node in front of / the reverse point
    # Hold keeps our place in the 2nd list so we can move toward the end of the list
    
    second = first.next
    slow = first.next = None
    while second:
        Hold = second.next
        second.next = slow
        slow = second
        second = Hold

    # Merge 1st list and now reversed 2nd list
    # first points back to list.head and second goes to slow which is the start of the 2nd list
    first = llist.head
    second = slow
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    # Printing the answer in a nicer format
    first = llist.head
    answer = []

    while first:
        answer.append(first.data)
        first = first.next

    return print(answer)


# Testing:

if __name__ == "__main__":
    llist = Linkedlist()
    llist.add_node(1)
    llist.add_node(2)
    llist.add_node(3)
    llist.add_node(4)
    llist.add_node(5)
    llist.print_llist()
    # reorder_bruteforce(llist)
    reorder_improved(llist)
    

