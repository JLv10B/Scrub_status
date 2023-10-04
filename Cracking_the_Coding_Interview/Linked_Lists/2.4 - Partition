"""
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Approach:
-Compare each node to the partition starting at the head (working left to right)
-Traverse the linked list until a node < partition node is found
-Move that node to the head and repeat

"""
from ParentLinkedList import LinkedList

# Set 2 pointers part and current_node to self.head
# While current_node exists
# If the current_node.data < x (partition value):
# Store the part data in storage and update it to current_node.data
# Update current_node.data with data stored in storage
# Move both pointers
# If the node.data >= x then only move current_node

class Partition(LinkedList):
    def partition(self, x):
        storage = []
        part = self.head
        current_node = self.head
        while current_node != None:
            if current_node.data < x:
                storage.append(part.data)
                part.data = current_node.data
                current_node.data = storage.pop()
                current_node = current_node.next
                part = part.next
            else:
                current_node = current_node.next


# Testing
llist = Partition()

llist.insertAtEnd(3)
llist.insertAtEnd(5)
llist.insertAtEnd(8)
llist.insertAtEnd(5)
llist.insertAtEnd(10)
llist.insertAtEnd(2)
llist.insertAtEnd(1)

print('Node data:')
llist.printLL()

print('Part at 5:')
llist.partition(5)
llist.printLL()