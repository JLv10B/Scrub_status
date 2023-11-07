class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # def __str__(self) -> str:
    #     return (f'{self.data}')

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBeginning
        else:
            while (current_node != None and position +1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next # Current_node.next points at the desired index
                current_node.next = new_node
            else:
                print('Index does not exist')

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_node(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next.next: # Traverses linked list until current_node is 2nd to last node
            current_node = current_node.next

        current_node.next = None # Removes the last node

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next