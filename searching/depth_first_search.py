# Depth First Search searchs vertically towards the bottom of a tree/graph
# Then comes back up to previous nodes to check for other paths down
# Pros : Uses Less Memory, Good at determining if Paths Exist
# Cons : Can become Slow in processing

# inorder, preorder, postorder types of returns

#     101 
#    /   \
#   /     \
# 33       105

# inorder : return would be [33, 101, 105]

# preorder : return would be [101, 33, 105]

# postorder : return would be [33, 105, 101]



# Converted from this Solution from JavaScript to Python from this lesson:
# https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12429754#questions

from collections import deque


class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if (self.root == None):
            self.root = newNode
        else:
            currentNode = self.root
            while(True):
                if(value < currentNode.value):
                    # Left
                    if(currentNode.left is None):
                        currentNode.left = newNode
                        return self
                
                    currentNode = currentNode.left
                else:
                    # Right
                    if(currentNode.right is None):
                        currentNode.right = newNode
                        return self

                    currentNode = currentNode.right


    def lookup(self, value):
        if (self.root is None):
            return False
    
        currentNode = self.root
        while(currentNode):
            if(value < currentNode.value):
                currentNode = currentNode.left
            elif(value > currentNode.value):
                currentNode = currentNode.right
            elif (currentNode.value == value):
                return currentNode

        return None

    def remove(self, value):
        if (self.root):
            return False
        currentNode = self.root
        parentNode = None
        while(currentNode):
            if(value < currentNode.value):
                parentNode = currentNode
                currentNode = currentNode.left
            elif(value > currentNode.value):
                parentNode = currentNode
                currentNode = currentNode.right
            elif (currentNode.value == value):
                # We have a match, get to work!
            
                # Option 1: No right child: 
                if (currentNode.right == None):
                    if (parentNode == None):
                        self.root = currentNode.left
                else:
                    
                    # if parent > current value, make current left child a child of parent
                    if(currentNode.value < parentNode.value):
                        parentNode.left = currentNode.left
                    
                    # if parent < current value, make left child a right child of parent
                    elif(currentNode.value > parentNode.value):
                        parentNode.right = currentNode.left
        
            
            # Option 2: Right child which doesnt have a left child
            elif (currentNode.right.left == None):
                if(parentNode == None):
                    self.root = currentNode.left
                else:
                    currentNode.right.left = currentNode.left
                
                # if parent > current, make right child of the left the parent
                if(currentNode.value < parentNode.value):
                    parentNode.left = currentNode.right
                
                # if parent < current, make right child a right child of the parent
                elif (currentNode.value > parentNode.value):
                    parentNode.right = currentNode.right
 
            
            # Option 3: Right child that has a left child
            else:

                # find the Right child's left most child
                leftmost = currentNode.right.left
                leftmostParent = currentNode.right
                while(leftmost.left is not None):
                    leftmostParent = leftmost
                    leftmost = leftmost.left
                
            
            # Parent's left subtree is now leftmost's right subtree
            leftmostParent.left = leftmost.right
            leftmost.left = currentNode.left
            leftmost.right = currentNode.right

            if(parentNode == None):
                self.root = leftmost
            else:
                if(currentNode.value < parentNode.value):
                    parentNode.left = leftmost
                elif(currentNode.value > parentNode.value):
                    parentNode.right = leftmost

        return True


    def BreadthFirstSearch(self):
        currentNode = self.root
        list = []
        queue = deque()
        queue.append(currentNode)

        while(len(queue) > 0):
            currentNode = queue.popleft()
            list.append(currentNode.value)
            if(currentNode.left):
                queue.append(currentNode.left)
            
            if(currentNode.right):
                queue.append(currentNode.right)

        return list
    
    def create_queue_for_recursive(self):
        currentNode = self.root
        queue = deque()
        queue.append(currentNode)

        return queue


    def BreadthFirstSearchR(self, queue, bfsr_list):
        if (len(queue) is None):
            return bfsr_list

        currentNode = queue.popleft()
        bfsr_list.append(currentNode.value)
        
        if (currentNode.left):
            queue.append(currentNode.left)
        if (currentNode.right):
            queue.append(currentNode.right)
        
        
        return self.BreadthFirstSearchR(queue, list)
    
    def depth_first_search_inorder(self):
        return traverse_inorder(self.root, [])
    

    def depth_first_search_postorder(self):
        return traverse_postorder(self.root, [])
    

    def depth_first_search_preorder(self):
        return traverse_preorder(self.root, [])


def traverse_inorder(node, dfs_list):
    if(node.left):
        traverse_inorder(node.left, dfs_list)
    dfs_list.append(node.value)
    if(node.right):
        traverse_inorder(node.right, dfs_list)

    return dfs_list

def traverse_preorder(node, dfs_list):
    dfs_list.append(node.value)
    if(node.left):
        traverse_preorder(node.left, dfs_list)
    if(node.right):
        traverse_preorder(node.right, dfs_list)

    return dfs_list

def traverse_postorder(node, dfs_list):
    if(node.left):
        traverse_postorder(node.left, dfs_list)
    if(node.right):
        traverse_postorder(node.right, dfs_list)

    dfs_list.append(node.value)

    return dfs_list
    
    


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

queue = tree.create_queue_for_recursive()

print('BFS', tree.BreadthFirstSearch())
# print('BFS', tree.BreadthFirstSearchR([tree.root], []))

print(tree.depth_first_search_inorder())
print(tree.depth_first_search_preorder())
print(tree.depth_first_search_postorder())

#      9
#   4     20
# 1  6  15  170

# DFS: InOrder, PreOrder, PostOrder

# InOrder : [1, 4, 6, 9, 15, 20, 170]
# PreOrder : [9, 4, 1, 6, 20, 15, 170]
# PostORder : [1, 6, 4, 15, 170, 20, 9]

def traverse(node):
    tree = node.value

    if node.left == None:
        tree.left = None
    else:
        tree.left(traverse(node.left))

    if node.right == None:
        tree.right = None
    else:
        tree.right = traverse(node.right)


    return tree