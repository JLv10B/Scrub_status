"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = [[]]
Output: []

Notes:
-We need to look at the first node in each list
-If there is a node that is smaller than all the other nodes then set that list as the 
master_list => list being merged into
-Create merge pointer that stays at the merge point
-Move compare pointer to the next node and compare values again
-If values are equal then put them both in after the merge pointer and move the merge pointer
-continue until all the compare pointers == None
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

def merge_sorted_lists(lists):
    # Base cases
    if len(lists) == 0 or len(lists) is None:
        return None
    
    # Merge 2 lists until there is only 1 list left in lists
    # return lists[0]
    while len(lists) > 1:
        list1 = lists.pop()
        list2 = lists.pop()
        lists.append(merge2lists(list1, list2))

    return lists[0]
        
def merge2lists(list1, list2):
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    
    if list1.data <= list2.data:
        list1.next = merge2lists(list1.next, list2)
        return list1
    else:
        list2.next = merge2lists(list1, list2.next)
        return list2

def report_list(list):
    if list is None:
        print('No nodes')

    current_node = list
    while current_node:
        print(current_node.data)
        current_node = current_node.next



# Testing:

if __name__ == "__main__":
    list1 = Linkedlist()
    list2 = Linkedlist()
    list3 = Linkedlist()
    list1.add_node(1)
    list1.add_node(4)
    list1.add_node(5)
    list2.add_node(1)
    list2.add_node(3)
    list2.add_node(4)
    list3.add_node(2)
    list3.add_node(6)
    lists = [list1.head, list2.head, list3.head]
    report_list(merge_sorted_lists(lists))