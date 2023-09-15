# Breadth First Search or BFS for short. 
# Searches Left to Right in Tree/Graph then change level
# Pros: Shortest Path, Closer Nodes
# Cons: Uses More Memory


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


    def BreadthFirstSearchR(self, queue, list):
        if (len(queue) is None):
            return list

        currentNode = queue.popleft()
        list.append(currentNode.value)
        
        if (currentNode.left):
            queue.append(currentNode.left)
        if (currentNode.right):
            queue.append(currentNode.right)
        
        
        return self.BreadthFirstSearchR(queue, list)


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
# print('BFS', tree.BreadthFirstSearchR(queue, []))

#      9
#   4     20
# 1  6  15  170

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






# from collections import deque

# # Binary Tree from Data Structure lesson
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def insert(node, value):
#     if node is None:
#         return Node(value)
#     if value > node.value:
#         node.right = insert(node.right, value)
#     elif value < node.value:
#         node.left = insert(node.left, value)
    
#     return node

# def search(node, value):
#     if node is None or node.value == value:
#         return node
#     if node.value > value:
#         return search(node.left, value)
        
#     return search(node.right, value)

# def print_tree(node):
#     if node.left:
#         print_tree(node.left)
#     print(node.value)
#     if node.right:
#         print_tree(node.right)

# def breadth_first_search(node):
#     currentNode = node  #.value
#     bfs_list = []
#     queue = deque()

#     queue.append(currentNode)

#     while(len(queue) > 0):
#         currentNode = queue.popleft()
#         print(currentNode.value)
#         bfs_list.append(currentNode.value)
#         if(currentNode.left):
#             queue.append(currentNode.left)
#         if(currentNode.right):
#             queue.append(currentNode.right)
#     return bfs_list


# def breadth_first_search_recursive(queue, bfs_list):

#     if(len(queue) is None):
#         return bfs_list
    
#     currentNode = queue.popleft()
#     bfs_list.append(currentNode.value)

#     if(currentNode.left):
#         queue.append(currentNode.left)
#     if(currentNode.right):
#         queue.append(currentNode.right)

#     return breadth_first_search_recursive(queue, bfs_list)

       



# tree = Node(9)

# insert(tree, 4)
# insert(tree, 6)
# insert(tree, 20)
# insert(tree, 170)
# insert(tree, 15)
# insert(tree, 1)
# print(breadth_first_search(tree))


# def create_queue(node):
#     currentNode = node  #.value
#     queue = deque()

#     queue.append(currentNode)

#     while(len(queue) > 0):
#         currentNode = queue.popleft()
#         print(currentNode.value)
#         if(currentNode.left):
#             queue.append(currentNode.left)
#         if(currentNode.right):
#             queue.append(currentNode.right)

#     return queue

# queue = create_queue(tree)

# print(breadth_first_search_recursive(queue, []))

# print()

