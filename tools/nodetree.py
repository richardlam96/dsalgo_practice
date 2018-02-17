# NODE BINARY TREE ###########################################################
# A binary tree that uses the Node class to perform operations. Most of the
# functions implemented here have O(logN) since they are all traversing
# through the binary tree which has a height close to logN.
#
# NOTE: about some of the functions:
#   - Probably the most important: The implementation of the insert function
#     does not allow duplicates in the tree. And this does not imply that
#     simply removing the respective conditional statements removes
#     this feature. (It wouldn't really change anything).
#     Perhaps a better way to deal with this is to have a Node implementation
#     that uses a tuple to store a data value and the number of occurences or
#     a dictionary with the same key and value pairs.
#     Turns out adding a data member in node for frequency turns the tree into
#     a Huffman Tree.
#
#   - The has() function works. Though there may be a simpler way to write it,
#     all the else: break's in there are necessary to get it working.
#     and _remove_two_child() uses the same structure.
#
#   - There are a good amount of protected functions to supplement other
#     functions just to make it more modular.
#
#   - The _remove_two_child() function includes an algorithm to find the
#     node-to-remove's successor, or the smallest value larger than itself.
#
#
# NOTE: This implementation of Node does not have a reference the the parent
# Node, so things will be done a little differently, especially with the
# remove functions. Might even be able to simplify it to one remove function
# with a reference to parent.
#

class Node(object):

    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None


class NodeTree(object):

    def __init__(self):
        self.head = Node()


    def has(self, value):
        """Essentially a binary search."""
        if self.head.data == None:
            return False

        current = self.head

        # traverse through tree
        while current.data != None:
            if value < current.data:
                if current.left:
                    current = current.left
                else:
                    break
            elif value > current.data:
                if current.right:
                    current = current.right
                else:
                    break
            elif value == current.data:
                return True
            else:
                break
        return False


    def insert(self, value):
        """Attempts to insert a given value, but returns if it is a dup."""
        current = self.head

        if current.data == None:
            current.data = value
            return True

        new_node = Node(value)

        while current != None:
            if value < current.data:
                if current.left == None:
                    current.left = new_node
                    return True
                current = current.left
            elif value > current.data:
                if current.right == None:
                    current.right = new_node
                    return True
                current = current.right
            elif value == current.data:
                return False



    def remove(self, value):
        """Removes given value if it can be found."""
        # find value with same algorithm as has() function
        current = self.head

        while current.data != None:
            if value < current.data:
                if current.left:
                    current = current.left
                else:
                    return False
            elif value > current.data:
                if current.right:
                    current = current.right
                else:
                    return False
            elif value == current.data:
                break
            else:
                return False


        # calls auxillary remove functions depending on case
        if current.left == None and current.right == None:
            self._remove_leaf(current)
        elif current.left == None or current.right == None:
            self._remove_one_child(current)
        elif current.left != None and current.right != None:
            self._remove_two_child(current)

        return True


    def _remove_leaf(self, trashnode):
        # leaf, so no left and right, just set to None
        trashnode.data = None   # not sure if this is necessary
        trashnode = None


    def _remove_one_child(self, trashnode):
        # if it only has one child, set current.data to child's and set
        # child to None
        # basically, copy the child to current
        replacement = Node()
        if trashnode.left != None:
            replacement = trashnode.left
        elif trashnode.right != None:
            replacement = trashnode.right

        trashnode.data = replacement.data
        trashnode.left = replacement.left
        trashnode.right = replacement.right
        replacement = None


    def _remove_two_child(self, trashnode):
        current = trashnode

        # traverse to leftmost node greater than the trashnode
        # to find successor
        current = current.right
        while current.left != None:
            current = current.left

        # replace value for trashnode
        trashnode.data = current.data

        # remove copied node
        if current.right != None:
            self._remove_one_child(current)
        elif current.right == None:
            self._remove_leaf(current)



    def get_array(self):
        ret = []
        self._get_array_aux(ret, self.head)
        return ret


    def _get_array_aux(self, ret, target):
        current = target

        if current.left:
            self._get_array_aux(ret, current.left)

        ret.append(current.data)

        if current.right:
            self._get_array_aux(ret, current.right)


