import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from red_black_tree import RedBlackBST


class RedBlackTreeSimpleTest(unittest.TestCase):
    
    def setUp(self):
        self.letters = 'searchxmpl'
        self.bst = RedBlackBST()
        for letter in self.letters:
            self.bst.put(letter, 1)

    def test_sorting(self):
        correct_order = sorted(self.letters)
        result_order = self.bst.get_keys()
        self.assertEqual(correct_order, result_order)

    def test_tree_size(self):
        correct_size = len(self.letters)
        result_size = self.bst.alt_size()
        self.assertEqual(correct_size, result_size)

if __name__ == '__main__':
    unittest.main()
