"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the 
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

def hasCycle(head):
    if head == None:
        return False
    
    visited = set()
    current_node = head
    visited.add(current_node)
    while current_node.next:
        if current_node.next not in visited:
            visited.add(current_node.next)
            current_node = current_node.next
        else:
            return True
    return False

def hasCycle_two_pointer(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False