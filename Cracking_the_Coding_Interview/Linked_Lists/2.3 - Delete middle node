"""
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

Input:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

"""

from ParentLinkedList import LinkedList

# Set input to current node
# If current node is not head or last node
# Traverse the linked list until current_node.next is input node
# Set current_node.next to current_node.next.next

class DeleteMiddle(LinkedList):
    def deletemiddle(self, node):
            node.data = node.next.data
            node.next = node.next.next

        
# Testing
llist = DeleteMiddle()

llist.insertAtEnd('1')
llist.insertAtEnd('2')
llist.insertAtEnd('3')
llist.insertAtEnd('4')
llist.insertAtEnd('5')
llist.insertAtEnd('6')

print('Node data:')
llist.printLL()

print('Delete 3:')
llist.deletemiddle(llist.head.next.next)
llist.printLL()