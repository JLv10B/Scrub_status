"""
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Notes:
-start at the head of each list
-as long as neither of the nodes is none add them
-If sum > 9 then use % 10 to get the single digit and add that as a node in the resultant linked list
-Because there is a loop we can use a helper function to perform this task
-If one of the nodes is None, if there is a remainder then add that to the other node and input that into the
result linked list
-If there is no remainder then input the remaining nodes into the resultant linked list
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

def add_two(num1, num2): 
    digits = []
    answer = Linkedlist()
    helper(num1.head, num2.head, digits, 0)

    for digit in digits:
        answer.add_node(digit)
    return answer.print_llist()
    
    
def helper(num1, num2, digits, remainder):
    # Adds the values of 2 nodes and saves the singles digit in [digits] and the tens digit in remainder
    if (num1 is None) and (num2 is None):
        if remainder > 0:
            digits.append(remainder)
        return digits

    # Sums non-None nodes to remainder
    new_digit = remainder    
    if num1:
        new_digit += num1.data
        num1 = num1.next
    if num2:
        new_digit += num2.data
        num2 = num2.next

    # If new_digit > 9 then set remainder to 1 and last_digit to new_digit % 10
    # if new_digit <= 9 then append to digits
    if new_digit > 9:
        last_digit = new_digit % 10
        remainder = 1
        digits.append(last_digit)
    else:
        remainder = 0
        digits.append(new_digit)

    helper(num1, num2, digits, remainder)

# Testing:

if __name__ == "__main__":
    num1 = Linkedlist()
    num2 = Linkedlist()
    num1.add_node(9)
    num1.add_node(9)
    num1.add_node(9)
    num1.add_node(9)
    num1.add_node(9)
    num1.add_node(9)
    num1.add_node(9)
    num2.add_node(9)
    num2.add_node(9)
    num2.add_node(9)
    num2.add_node(9)
    # num1.print_llist()
    # num2.print_llist()
    add_two(num1, num2)
    