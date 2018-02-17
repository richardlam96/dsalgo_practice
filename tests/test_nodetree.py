import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from numpy import random

from nodetree import NodeTree


class NodeTreeTests(unittest.TestCase):
    """
    General testing base for testing insertion, removal, validity of random values.
    """

    def setUp(self):
        self.sample_tree = NodeTree()
        self.target_sm = [i for i in range(20)]
        random.shuffle(self.target_sm)

        # inserting here makes more sense for further testing
        for val in self.target_sm:
            self.sample_tree.insert(val)


    def test_existing_values(self):
        # check all values with get_array()
        self.assertEqual(sorted(self.target_sm), self.sample_tree.get_array())

        # check all values with has()
        for val in self.target_sm:
            self.assertTrue(self.sample_tree.has(val))

        # check has() works for an absurd value not in the tree
        self.assertFalse(self.sample_tree.has(100000000000000000000000))


    def test_remove_beginning(self):
        # remove values 0 to 4 from the tree
        for val in self.target_sm[:5]:
            self.sample_tree.remove(val)
            self.assertFalse(self.sample_tree.has(val))


    def test_remove_end(self):
        # remove values 5 to 9 from the tree
        for val in self.target_sm[-5:]:
            self.sample_tree.remove(val)
            self.assertFalse(self.sample_tree.has(val))


    def test_remove_random(self):
        # remove random value to test each type of remove
        val = random.randint(0, 10)
        self.sample_tree.remove(val)

        self.assertFalse(self.sample_tree.has(val))


    def test_remove_nonexist_val(self):
        self.assertFalse(self.sample_tree.remove(100000000000000000000000000))



class NodeTreeTestWithDuplicates(NodeTreeTests):
    """
    Test class that inherits from the above 'base' class but uses a target with
    duplicate values.

    With the current implementation of NodeTree however, this is will not work.
    Probably more accurate to test distinct values.
    """

    def setUp(self):
        self.sample_tree = NodeTree()
        self.target_sm = []
        for i in range(5):
            for _ in range(i):
                self.target_sm.append(i)
        random.shuffle(self.target_sm)

        for val in self.target_sm:
            self.sample_tree.insert(val)


    def test_existing_values(self):
        super().test_existing_values()






if __name__ == '__main__':
    unittest.main()
