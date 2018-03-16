# BINARY SEARCH TREE SYMBOL TABLE ############################################
# Compared to the other implementation of a Symbol Table, this implementation 
# uses a Node class to store two pointers: a left pointer to point to a
# smaller key value, and a right pointer to point to a bigger key value than
# the current Node's value.
# Also, this implementation will not use rank() and select() methods.
# 
# The text uses recursive methods to keep things consistent, but a good
# exercises is to implement them without recursion, which is how elementary
# BST's are implemented, and without a counter for each Node.
#
# First, do it recursively, for the recursion practice, then do it non-
# recursively.
#

class Node(object):
    """
    Node that stores a key-value pair and two pointers to other Nodes.
    """
    def __init__(self, key=None, value=None):
       self.key = key
       self.value = value
       self.left = None
       self.right = None



class BinaryST(object):
    """
    Search Tree made of Nodes with methods using the basic binary search
    algorithm.
    """
    
    def __init__(self):
        self.root = Node()


    def size(self):
        """
        Recursion starter for finding tree size.
        """
        if self.root == None:
            return 0
        return self.size(self.root)


    def recur_size(self, target_node):
        """
        Directly recursive function to find the number of nodes under the 
        given node as root including itself.
        """
        if target_node == None:
            return 0
        left_size = self.recur_size(target_node.left)
        right_size = self.recur_size(target_node.right)
     
        return 1 + left_size + right_size
    

    def put(self, key, value):
        """
        Recursion starter for adding a value or updating if exists.
        """
        if self.root == None:
            return Node(key, value)
        self.recur_put(self, self.root, key, value)


    def recur_put(self, node, key, value):
        """
        Directly recursive function to add or update the given key with given
        value..
        """
        if node.key == None:
            return Node(key, value)
        if key < node.key:
            node.left = self.recur_put(node.left, key, value)
        elif key > node.key:
            node.right = self.recur_put(node.right, key, value)
        else:
            node.value = value
       
        return node




