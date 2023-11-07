"""
Implement a function to check if a linked list is a palindrome.

Input: a -> s -> d -> s -> a

Output: True
"""
from ParentLinkedList import LinkedList

def palindrome_iter(llist):
    """
    -Take the first half of the list and store it in reverse then compare it with the 2nd half of the list so
    you only have to iterate through the list once. 
    -For odd nodes skip the middle node.
    -Slow moves 1, fast moves 2 nodes and when fast hits the end of the list or can't move
    -If fast is at the end of the list -> odd nodes -> skip the middle node
    """
    half = []
    slow = llist.head
    fast = llist.head
    while fast and fast.next:
        half.append(slow)
        slow = slow.next
        fast = fast.next.next
        # print(f'slow: {slow.data}, fast: {fast.data}, half: {half}')

    if fast: 
        slow = slow.next

    while slow:
        top = half.pop()
        if top.data != slow.data:
            return False
        slow = slow.next
    return True

# Testing:

if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtEnd(2)
    llist.insertAtEnd(2)
    llist.insertAtEnd(2)
    llist.insertAtEnd(1)
    print(palindrome_iter(llist))