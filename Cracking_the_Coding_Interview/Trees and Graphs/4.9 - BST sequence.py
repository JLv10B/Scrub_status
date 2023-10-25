"""
A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

Ex.
Input: 
                    50 
        20                    60
    10                  55
Output: [50,20,60,10,55], [50,60,20,10,55], [50,20,60,55,10], [50,60,20,55,10]

Approach:
-We can think of the output as every variation of:
    [
    {root},
    {1st depth in any order},
    {2nd depth in any order},
    ...
    ]
-Need a function which does a breadth first search and creates a list of dictionaries for each depth
-Need a function which utilizes the output from the first function and creates unique lists

"""
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            if current.key > key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def get_node(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current

            if current.key > key:
                current = current.left
            else:
                current = current.right
        raise Exception("No such value in the tree")
    
def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        # print(f'Right: {right}, Right_sequence: {right_sequences}')
        for left in left_sequences:
            # print(f'Left: {left}, Left_sequence: {left_sequences}')
            sequences = weave(left, right, [node.key], sequences)
            # print(f'Node: {node.key}, Sequence: {sequences}')
    return sequences


def weave(first, second, prefix, results):
    # print(f'First array: {first}, Second array:{second}')
    if len(first) == 0 or len(second) == 0:
        
        result = prefix.copy()
        # result = prefix
        print(f'result: {result}')
        result.extend(first)
        result.extend(second)
        results.append(result)
        # print(f'Base case: {results}')
        return results

    head = first[0]
    # print(f'Head of first: {head}')
    prefix.append(head)
    # print(f'Prefix after append head: {prefix}')
    results = weave(first[1:], second, prefix, results)
    # print(f'First recursion complete: {results}')
    prefix.pop()
    # print(f'Prefix after pop: {prefix}')
    head = second[0]
    # print(f'Head of second: {head}')
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results


def find_bst_sequences_backtracking(bst):
    if not bst.root:
        return []

    ret_backtracking = []

    def backtracking(choices, weave):
        if not len(choices):
            ret_backtracking.append(weave)
            return

        for i in range(len(choices)):
            nextchoices = choices[:i] + choices[i + 1 :]
            if choices[i].left:
                nextchoices += [choices[i].left]
            if choices[i].right:
                nextchoices += [choices[i].right]
            backtracking(nextchoices, weave + [choices[i].key])

    backtracking([bst.root], [])
    return ret_backtracking


testable_functions = [find_bst_sequences, find_bst_sequences_backtracking]


def test_find_bst_sequences():
    for find_bst in testable_functions:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        sequences = find_bst(bst)
        assert [2, 1, 3] in sequences
        assert [2, 3, 1] in sequences
        assert len(sequences) == 2


def example():
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);

    sequences = find_bst_sequences(bst)
    print(sequences)

    sequences = find_bst_sequences_backtracking(bst)
    print(sequences)


if __name__ == "__main__":
    example()