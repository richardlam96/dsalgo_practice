# RED BLACK TREE #############################################################
# A binary search tree that is based on the 2-3 tree and the standard binary
# search tree.
#
# It maintains tree balance like the 2-3 tree, so searching times can remain
# consistent and independent of the order of elements from input. It also
# maintains 'black balance', which is the number of black colored paths that
# it takes to get from the queried node to the root and stays the same for 
# each node.
#
# The node model used will include a key value pair, two links to other nodes,
# a 'color' boolean value, and an integer value to store the number of nodes
# in the subtree (which is an alternative to a recursive calculation).
#
# The most notable functions will the inserts, rotations, and the color flip.
#

class Node(object):
    def __init__(self, key=None, value=None,
                 color=True):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.N = 1


class RedBlackBST(object):
    def __init__(self):
        self.root = None
        self.trash = None   # temp var to keep deleted successor
                            # while del_min will just make sure tree is set
                            # properly after removing successor

    def is_red(self, node):
        if not node:
            return False
        return node.color

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def put(self, key, value):
        self.root = self.recur_put(self.root, key, value)
        self.root.color = False

    def recur_put(self, node, key, value):
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self.recur_put(node.left, key, value)
        elif key > node.key:
            node.right = self.recur_put(node.right, key, value)
        else:
            node.value = value

        
        if not self.is_red(node.left) and self.is_red(node.right):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        # do the rotations mess up the node count?
        node.N = self.size(node.left) + self.size(node.right)
        return node
            
    def print_keys(self, node=None):
        if not node: 
            node = self.root
        if node.left:
            self.print_keys(node.left)
        print(node.key)
        if node.right:
            self.print_keys(node.right)
   
    def get_keys(self):
        ret_list = []
        self.recur_get_keys(self.root, ret_list)
        return ret_list

    def recur_get_keys(self, node, ret_list):
        if node.left:
            self.recur_get_keys(node.left, ret_list)
        ret_list.append(node.key)
        if node.right:
            self.recur_get_keys(node.right, ret_list)

    def size(self, node):
        if not node:
            return 0
        else:
            return node.N

    def alt_size(self):
        ret = self.recur_size(self.root)
        return ret

    def recur_size(self, node):
        if not node:
            return 0
        return self.recur_size(node.left) + self.recur_size(node.right) + 1

    def delete(self, key):
        # find node with given key
        current_node = self.root
        while key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            elif key == current_node.key: 
                break
            else:
                return False

        old_node = current_node
        current_node = self.delete_min(current_node)
        return old_node 

    def delete_min(self, node=None):
        if not node:
            node = self.root
        # need to handle all node == root cases here?
        if node = self.root:
            if node == self.root:
                if self.is_2node(node.left) and self.is_2node(node.right):
                    self.flip_colors(node)
                    node.color = False
                if self.is_2node(node.left) and not self.is_2node(node.right):
                    self.rotate_left(node)

        # if it doesn't have a right, need to just return right as successor
        successor = self.recur_delete_min(node.right);
        successor.left = node.left
        successor.right = node.right
        return successor

    def recur_delete_min(self, node):
        # what you're really doing is moving the node up
        if not node.left:
            if node.right:
                return node.right
            return node

        # traverse down the left side of the tree while reorganizing
        if node.left and node.right:
            if not self.is_2node(node.left):
                pass
            else:
                if not self.is_2node(node.right):
                    node.right = self.rotate_right(node.right)
                    node = self.rotate_left(node)
                else: 
                    self.flip_colors(node)
        
        node.left = self.recur_delete_min(node.left)
        # check if successor is the min
        # successor = self.delete_min(node.left)
        # if not successor.left: 
        #     if successor.right:
        #         node.left = successor.right
        #     return successor

        # coming back up, turn 4-nodes back to 2-nodes
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)
        return node

       # elif self.is_2node(node):
        #     self.delete_min(node.left)

        #     if self.is_2node(node.left) and not self.is_2node(node.left.left):
        #         node.left.left.color = True
        #         node.left.left.left = False

        #     # this is a problem given the conditional:
        #     # if the node is not a 2 node, there is nothing to do
        #     # unless you save the condition for last?
        #     if (not self.is_2node(node) and 
        #        self.is_2node(node.left.left) and
        #        self.is_2node(node.left.right)): 
        #         self.flip_colors(node.left)

    def is_2node(self, node):
        if not node or not node.left:
            return False
        return not self.is_red(node.left)






































