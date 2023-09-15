class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


def insert(node, value):
    if node is None:
        return Node(value)      
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    
    return node
    

def search(node, value):
     
    #  if node is None:
    #       return 'Value not in Tree' 
     
    #  if node.value == value:
    #       return node.value
     
    if node is None or node.value == value:
        return node

    if node.value < value:
        return search(node.right, value)
    
    return search(node.left, value)

def print_tree(node):
    if node.left:
        print_tree(node.left)
    print(node.value)
    if node.right:
        print_tree(node.right)



binary_tree = Node(50)
insert(binary_tree, 30)
insert(binary_tree, 20)
insert(binary_tree, 40)
insert(binary_tree, 70)
insert(binary_tree, 60)
insert(binary_tree, 80)

# print_tree(binary_tree)

# print(search(binary_tree, 20))
# print(search(binary_tree, 0))

search_value = 20

if search(binary_tree, search_value) is None:
    print(search_value, 'not found')
else:
    print(search_value, 'found')

search_value = 0

if search(binary_tree, search_value) is None:
    print(search_value, 'not found')
else:
    print(search_value, 'found')


#     def insert(self, value):
#         if self.value:
#             if value < self.value:
#                 if self.left is None:
#                     self.left = BinaryTree(value)
#                 else:
#                     self.left.insert(value)
#             elif value > self.value:
#                 if self.right is None:
#                     self.right = BinaryTree(value)
#                 else:
#                     self.right.insert(value)

#         else:
#             self.value = value

#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.value)
#         if self.right:
#             self.right.print_tree()

                      
# root = BinaryTree(100)

# root.print_tree()

# root.insert(50)
# root.insert(55)
# root.insert(60)

# root.print_tree()