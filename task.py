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
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False  # Avoids duplicate
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
        if node is None:
            return 0
        height_left = self.tree_height(node.left) + 1
        height_right = self.tree_height(node.right) + 1
        return max(height_left, height_right)

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