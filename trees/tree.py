class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value > node.value:
        node.right = insert(node.right, value)
    elif value < node.value:
        node.left = insert(node.left, value)
    
    return node

def search(node, value):
    if node is None or node.value == value:
        return node
    if node.value > value:
        return search(node.left, value)
        
    return search(node.right, value)

def print_tree(node):
    if node.left:
        print_tree(node.left)
    print(node.value)
    if node.right:
        print_tree(node.right)


input = [1,2,3,4,5]

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

print_tree(binary_tree)

# for item in range(len(input)):

dict()
# print(input.pop())

# tree = Node(input)
# print(search(tree, 3))

tree = None
count = 0
while(len(input) > count):
    tree = insert(tree, input[count])
    print(input[count])
    # input.pop(0)
    count += 1

# print(search(tree, 2))
# print(search(tree, 20))

if search(tree, 2) is None:
    print(f'{2} was not found')
else:
    print(f'{2} was found')

if search(tree, 20) is None:
    print(f'{20} was not found')
else:
    print(f'{20} was found')

print_tree(tree)