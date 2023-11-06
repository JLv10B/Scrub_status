"""
You have two numbers represented by a linked list, where each node contains a single
digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
"""
from ParentLinkedList import LinkedList, Node

class Number(LinkedList):
    def add_digits_backward(self, number):
        digits = []
        
        while number >= 1:
            last_digit = number % 10
            digits.append(last_digit)
            # print(digits)
            number = number // 10

        self.head = Node(digits.pop(0))
        current_node = self.head

        for node in digits:
            new_node = Node(node)
            current_node.next = new_node
            current_node = current_node.next
    
    def add_digits_forward(self, number):
        digits = []
        
        while number >= 1:
            last_digit = number % 10
            digits.append(last_digit)
            # print(digits)
            number = number // 10

        self.head = Node(digits.pop())
        current_node = self.head

        for index in range(len(digits)-1, -1, -1):
            new_node = Node(digits[index])
            current_node.next = new_node
            current_node = current_node.next

def sum_llist_backwards(list1, list2, remainder=0):
    digits = []
    new_list = Number()
    helper_back(list1, list2, digits, 0)
    for digit in digits:
        new_list.insertAtEnd(digit)

    return new_list.printLL()

def helper_back(list1, list2, digits, remainder=0):
    if (list1 is None) and (list2 is None):
        if remainder == 1:
            digits.append(1)
            return digits
        return digits
    
    new_digit = remainder
    if list1:
        new_digit += list1.data
    if list2:
        new_digit += list2.data

    if new_digit > 9:
        last_digit = new_digit % 10
        digits.append(last_digit)
        remainder = 1
    else:
        digits.append(new_digit)
        remainder = 0

    if list1 and list1.next:
        first = list1.next
    else:
        first = None
    if list2 and list2.next:
        second = list2.next
    else:
        second = None
    helper_back(first, second, digits, remainder) 
    
    
            
# Testing:
first = 9999
second = 111
llist = Number()
llist.add_digits_backward(first)
# llist.printLL()
second_llist = Number()
second_llist.add_digits_backward(second)
# second_llist.printLL()
sum_llist_backwards(llist.head, second_llist.head)
print(first + second)