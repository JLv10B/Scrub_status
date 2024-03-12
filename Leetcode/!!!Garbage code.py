"""
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

def add_two_linked_lists(l1_head, l2_head):
    """
    This function adds 2 numbers and returns the sum as a linked list. 
    
    This function accepts 2 linked lists representing 2 non-negative integers who's digits are stored in reverse order, each node contains a single digit. Neither input can contain any leading zeros except the number 0 itself.

    Approach:
    - The head of each linked list is the single's place. Therefore if the sum of 2 nodes is > 9 then the 1 can be carried over to the next nodes.
    - Initialize linked_list_sum = Linkedlist(), carry_over = 0, l1_node = l1_head, l2_node = l2_head
    - Continue to loop through l1 and l2 nodes until you reach the tail for both and there is no carry_over to add
        - If l1_node is None then set l1_node_val to 0 and l1_node = None, else l1_node_val = l1_node.val, l1_node = l1_node.next
        - Repeat for l2_node
        - Add l1_node_val, l2_node_val, and carry_over to get new_node
        - If new_node is > 9: carry_over = 1, new_node-= 10, linked_list_sum.add_node(new_node)
        - Else carry_over = 0, linked_list_sum.add_node(new_node)
    
    """
    linked_list_sum = Linkedlist()
    carry_over = 0
    l1_node, l2_node = l1_head, l2_head

    while l1_node != None or l2_node != None or carry_over != 0:
        if l1_node == None:
            l1_node_val = 0
            l1_node = None
        else: 
            l1_node_val = l1_node.val
            l1_node = l1_node.next

        if l2_node == None:
            l2_node_val = 0
            l2_node = None
        else: 
            l2_node_val = l2_node.val
            l2_node = l2_node.next

        new_node = l1_node_val + l2_node_val + carry_over

        if new_node > 9:
            carry_over = 1
            new_node -= 10
        else:
            carry_over = 0
        linked_list_sum.add_node(new_node)

    return linked_list_sum.print_llist()

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Linkedlist:
    """
    Methods:
    --------
    add_node - adds a node as the head if self.head == None or to the end of the linked list
    print_llist - prints linked list
    """

    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node

    def print_llist(self):
        if self.head == None:
            return None
        
        current_node = self.head
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next

# Testing
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
    add_two_linked_lists(num1.head, num2.head)