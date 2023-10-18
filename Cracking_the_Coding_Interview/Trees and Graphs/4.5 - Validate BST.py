"""
Implement a function to check if a binary tree is a binary search tree

"""
def validate(root):
    def valid_bst(node, min, max):
        if node is None:
            return True
        
        if node.data < min or node.data > max:
            return False
        
        return (valid_bst(node.left, min, node.data) and valid_bst(node.right, node.data, max))
    return valid_bst(root, float('-inf'), float('inf'))
        
