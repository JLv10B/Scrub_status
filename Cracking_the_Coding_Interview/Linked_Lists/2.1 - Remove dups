"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

"""
from ParentLinkedList import LinkedList

# Initiate dictionary to hold values, starts with head.data
# Traverse through list
# Start at the head of the linked list and traverse until there is no self.next
# If self.next.data is not in dictionary then add and continue
# If self.next.data is in dictionary then replace self.next with self.next.next
class RemoveDuplicates(LinkedList):
    def removeDuplicates(self):
        if self.head == None:
            return self
        values = {self.head.data:1}
        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data not in values:
                values[current_node.next.data] = 1
                current_node = current_node.next
            else:
                current_node.next = current_node.next.next

# Testing
llist = RemoveDuplicates()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtEnd('c')
llist.insertAtEnd('d')
llist.insertAtEnd('d')
llist.insertAtEnd('d')

print('Node data:')
llist.printLL()

print('Removing duplicates:')
llist.removeDuplicates()
llist.printLL()
