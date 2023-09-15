# Manual build of Linked List from Real Python
# https://realpython.com/linked-lists-python/

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node 
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception("Node with data '%s' not found " % target_node_data)


    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head   
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
        
        raise Exception("Node with data '%s' not found " % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found " % target_node_data)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None # Add this to turn into Doubly Linked List

    def __repr__(self):
        return self.data
    

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))



llist = LinkedList()

print(llist)


first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node

print(llist)


# Traversing Linked List using __iter__

llist2 = LinkedList(["a","b","c","d","e"])
print(llist2)

for node in llist2:
    print(node)


# Using add_first function

llist3 = LinkedList()

llist3.add_first(Node("b"))
print(llist3)

llist3.add_first(Node("a"))
print(llist3)

# Using add_last function

llist3.add_last(Node('e'))
print(llist3)

llist3.add_last(Node('f'))
print(llist3)

# Using add_after function

llist4 = LinkedList()
try:
    llist4.add_after("a", Node("z"))
    print(llist4)
except Exception as e:
    print(e)

llist4 = LinkedList(["a", "b", "c", "d"])
print(llist4)

try:
    llist4.add_after("c", Node("cc"))
    print(llist4)
except Exception as e:
    print(e)


try:
    llist4.add_after("f", Node("g"))
    print(llist4)
except Exception as e:
    print(e)

# Using add_before function

try:
    llist5 = LinkedList()
    llist5.add_before("a", Node("a"))
except Exception as e:
    print(e)

llist5 = LinkedList(["b", "c"])
print(llist5)

llist5.add_before("b", Node("a"))
print(llist5)

llist5.add_before("b", Node("aa"))
llist5.add_before("c", Node("bb"))
print(llist5)

try:
    llist5.add_before("n", Node("m"))
    print(llist5)
except Exception as e:
    print(e)


# Using remove_node function

try:
    llist6 = LinkedList()
    llist4.remove_node("a")
    print(llist6)
except Exception as e:
    print(e)

llist6 = LinkedList(["a", "b", "c", "d", "e"])
print(llist6)

llist6.remove_node("a")
print(llist6)

llist6.remove_node("e")
print(llist6)

llist6.remove_node("c")
print(llist6)

try:
    llist6.remove_node("a")
    print(llist6)
except Exception as e:
    print(e)


# Circular Linked List

circular_llist = CircularLinkedList()
circular_llist.print_list()


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
d.next = a

circular_llist.head = a
circular_llist.print_list()

circular_llist.print_list(b)

circular_llist.print_list(d)