import math

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    



class Solution:

    # Approach 1: Top Down DFS O(n), uses recursion
    def isValidBST1(root: TreeNode) -> bool:

        # Function to validate passes node, low int for left comparison, 
        # high int for right comparison
        def validate(root: TreeNode, low: int, high: int) -> bool:
            # A root being null or None is valid
            if root is None:
                return True
            # These two if statements check the starting node value 
            # against starting low and high values, should be between them
            if (low is not None and root.val <= low):
                return False
            if ((high is not None and root.val >= high)):
                return False
            
            # Runs the validation against the left side and the right side
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)

        # Runs first pass of validate with TreeNode, math is a
        # Python system library that has to be imported
        # math is used to produce a negative infinity for initial low
        # and produce a posititve infinity for initial high
        return validate(root, -math.inf, math.inf)
    


    # # Approach 2: InOrder DFS O(n)

    # prev = int

    # def isValidBST2(root: TreeNode) -> bool:
    #     prev = None
        
    
    #     def inorder(root: TreeNode) -> bool:
    #         if root is None:
    #             return True
    #         if inorder(root.left) is False:
    #             return False
    #         if prev is not None and root.val <= prev:
    #             return False
            
    #         prev = root.val

    #         return inorder(root.right)

    #     return inorder(root)



def insert(node : TreeNode, value):
    if node is None:
        return TreeNode(value)
    if value > node.val:
        node.right = insert(node.right, value)
    elif value < node.val:
        node.left = insert(node.left, value)
    
    return node 

def print_tree(node : TreeNode):
    if node.left:
        print_tree(node.left)
    print(node.val)
    if node.right:
        print_tree(node.right)
        
def dfs_inorder(node):
    return traverse_inorder(node, [])


def traverse_inorder(node, dfs_list):
    if node.left:
        traverse_inorder(node.left, dfs_list)
    dfs_list.append(node.left)
    if node.right:
        traverse_inorder(node.right, dfs_list)

    return dfs_list



new_tree = TreeNode(50)
insert(new_tree, 20)
insert(new_tree, 30)
insert(new_tree, 17)
insert(new_tree, 5)
insert(new_tree, 60)


print_tree(new_tree)

print(Solution.isValidBST1(new_tree))
# print(Solution.isValidBST2(new_tree))