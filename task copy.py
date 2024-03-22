class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
    ######   Make changes if it is necessary     ######
    ###                                             ###
    ###                                             ###
    ###################################################
        new_node = Node(value)
        if self.root is None:
            self.height = 1
            self.root = new_node
            return True
        height = 1
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Avoids duplicate
            height = height + 1
            if height > self.height:
                self.height = height
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def tree_height(self, node):
        return self.height
    ######         Write your program here       ######
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###                                             ###
    ###################################################

# Create a BinarySearchTree instance
my_tree = BinarySearchTree()

# Input string
input_str = input()
numbers = [int(n) for n in input_str.split()]

# Building the BST from input
for number in numbers:
    my_tree.insert(number)

# Calculating the height of the BST
height = my_tree.tree_height(my_tree.root)
print(height)