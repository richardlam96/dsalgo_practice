import unittest
import string
import sys 
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from numpy import random

from binary_st import BinaryST



class BinaryTreeTests(unittest.TestCase):

    def setUp(self):
        self.sample_bst = BinaryST()
        mixed_alphabet = list(string.ascii_uppercase)
        random.shuffle(mixed_alphabet)
        for i, char in enumerate(mixed_alphabet):
            self.sample_bst.put(char, i)
        
    def test_put_and_get_keys(self):
        key_list = self.sample_bst.get_keys('A', 'Z')
        self.assertEqual(list(string.ascii_uppercase), key_list)

    def test_min_and_max_value(self):
        self.assertEqual('A', self.sample_bst.min().key)
        self.assertEqual('Z', self.sample_bst.max().key)

    def test_delete_min(self):
        self.sample_bst.delete_min()
        key_list = self.sample_bst.get_keys('A', 'Z')
        self.assertEqual(list(string.ascii_uppercase)[1:], key_list)

    def test_delete_random_values(self):
        bad_keys = []
        for i in random.choice(25, 5):
            self.sample_bst.delete(list(string.ascii_uppercase)[i])
            bad_keys.append(list(string.ascii_uppercase)[i])

        for key in bad_keys:
            self.assertFalse(key in self.sample_bst.get_keys('A', 'Z'))
            self.assertRaises(AttributeError)



if __name__ == '__main__':
    unittest.main()

