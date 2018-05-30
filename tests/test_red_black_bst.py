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

    def test_delete_min(self):
        correct_array = sorted(self.letters)
        correct_array.remove('a')
        self.bst.delete_min(self.bst.root)
        result_array = self.bst.get_keys()
        self.assertEqual(correct_array, result_array)

    def test_delete_min_value(self):
        correct_value = 'a'
        result_value = self.bst.delete_min().key
        self.assertEqual(correct_value, result_value)

    def test_delete_value_in_middle(self):
        correct_array = sorted(self.letters)
        correct_array.remove('r')
        self.bst.delete('r')
        result_array = self.bst.get_keys()
        self.assertEqual(correct_array, result_array)
        


if __name__ == '__main__':
    unittest.main()
