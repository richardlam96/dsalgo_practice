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
        self.root = None


    def size(self):
        """
        Recursion starter for finding tree size.
        """
        if self.root == None:
            return 0
        return self.recur_size(self.root)


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
            self.root = Node(key, value)
            return
        self.root = self.recur_put(self.root, key, value)


    def recur_put(self, node, key, value):
        """
        Directly recursive function to add or update the given key with given
        value..
        """
        if node == None:
            node = Node(key, value)
            return node 
        if key < node.key:
            node.left = self.recur_put(node.left, key, value)
        elif key > node.key:
            node.right = self.recur_put(node.right, key, value)
        else:
            node.value = value
       
        return node


    def min(self, key=None):
        if self.root == None:
            return None
        
        if not key:
            key = self.root

        traveling = key
        while traveling.left:
            traveling = traveling.left
        
        return traveling

    
    def max(self, key=None):
        if self.root == None:
            return None

        if not self.root.right:
            if self.root.left:
                return self.root.left
            return self.root

        if not key:
            key = self.root

        traveling = key
        while traveling.right:
            traveling = traveling.right

        return traveling


    def delete(self, key):
        # Problem here is setting variables to None does not delete the actual
        # node, it just deletes the variable that is referencing it. Seems like
        # one would need to catch the parent node to the node to be deleted
        # because garbage collection will activate when nothing is pointing to
        # that node.

        if self.root == None:
            return None

        traveling = self.root
        # Basic solution:
        # check if traveling is equal
        # else check if less or greater
        # then check if travel is equal to corres.
        # if any matches, break
        # else, move to corres. direction
        # 
        # if key is found
        # if no children, delete reference to it
        # find successor
        # 
        while traveling:
            if key < traveling.key:
                traveling = traveling.left
            elif key > traveling.key:
                traveling = traveling.right
            else:
                break

        # switch key and value for simplicity
        # then delete the min(traveling.right)
        if traveling:
            # no children, aka leaf
            if not (traveling.left and traveling.right):
                traveling = None
                return

            successor = self.min(traveling.right)
            # if no right child
            if not successor:
                traveling = traveling.left

            # else copy values
            else:
                traveling.key = successor.key
                traveling.value = successor.value
            
                successor = None
        return


    def print(self):
        if self.root == None:
            return ""

        self.recur_print(self.root)


    def recur_print(self, node):
        if node == None:
            return ""
   
        if node.left:
            self.recur_print(node.left)
        print(node.key, node.value)
        if node.right:
            self.recur_print(node.right)


    