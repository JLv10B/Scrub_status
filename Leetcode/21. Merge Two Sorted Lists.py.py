# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        """ You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.Return the head of the merged linked list.
        
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        
        Input: list1 = [], list2 = []
        Output: []
        
        Input: list1 = [], list2 = [0]
        Output: [0]
        
        """
        # If list1 or list2 is empty, return the list that is not empty.
        if list1 == None or list2 == None:
            return list1 or list2
        
        # Compare the node value from list1 and list2, if list1.val is less than or equal to 
        # list2.val then use list1.val as the listnode. Recursively go through the function to 
        # find list1.next or list2.next.
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
           
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
