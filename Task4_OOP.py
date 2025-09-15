# TASK 4 #

# This is NOT a binary search tree.
# In a BST, all values in the left subtree must be less than the node,
# and all values in the right subtree must be greater.
# Node 41 is in the left of 30, but 41 > 30 — so it's not a valid BST.


# define the Node class (given in Appendix B)
class Node:
    def __init__(self, val, l=None, r=None):
        self.value = val        # node value
        self.left = l           # left child
        self.right = r          # right child

    def __str__(self):
        # returns string version of the tree
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return str(self.value) + '({})({})'.format(
                str(self.left) if self.left is not None else '',
                str(self.right) if self.right is not None else '')

    # in-order depth-first traversal that prints True if the value is even, False otherwise
    def in_order_even_check(self):
        if self.left:
            self.left.in_order_even_check()
        print(self.value % 2 == 0)
        if self.right:
            self.right.in_order_even_check()

# define Search_tree class with insert method that raises error on duplicates
class Search_tree:
    def __init__(self):
        self.root = None  # tree starts empty

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value == current_node.value:
            # raise error if the value already exists in the tree
            raise ValueError('duplicate values are not allowed')
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

# create the tree using the Node class
my_tree = Node(20,
               Node(15,
                    Node(10),
                    Node(17)),
               Node(30,
                    Node(41)))
print(my_tree)

# in-order traversal: prints True if the node value is even, False otherwise
print('In-order even check:')
my_tree.in_order_even_check()