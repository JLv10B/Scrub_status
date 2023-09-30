"""
Implement an algorithm to find the kth to last element of a singly linked list.

Input:
Linked List: 1->2->3->4->5->6
k = 0
k = 1
k = 2
assume size is not known

Output:
6
5
4

Approach 1:
-Traverse through the list to find the last element count
-Travers to the kth element
-Seems like way too much work

Approach 2:
-Have 2 pointers, set them k elements apart
-Increment both of them until the faster pointer reaches the last element
-Return the first pointer

"""

from ParentLinkedList import LinkedList

# Initiate 2 pointers, both point to head
# Set variable to hold distance of fast and slow pointers
# Move fast pointer until pointers are k elements apart
# Move both pointers until there is no next node for the fast pointer indicating that it's at the end of the list
# Return the element at the slow pointer
class Kthtolast(LinkedList):
    def kthtolast(self, k):
        if self == None:
            print('Empty List')
            return
        
        fast = self.head
        slow = self.head
        distance = 0

        while distance < k:
            fast = fast.next
            distance += 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        print(f'The {k}th to last element is:', slow.data)

# Testing
llist = Kthtolast()

llist.insertAtEnd('1')
llist.insertAtEnd('2')
llist.insertAtEnd('3')
llist.insertAtEnd('4')
llist.insertAtEnd('5')
llist.insertAtEnd('6')

print('Node data:')
llist.printLL()

llist.kthtolast(0)
llist.kthtolast(1)
llist.kthtolast(2)

