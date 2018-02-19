import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from huffman import HuffmanMachine
from huffman import Node

class HuffmanTestBase(unittest.TestCase):
    """
    Test the Huffman Machine against some input.
    """

    def setUp(self):
        self.sample_input = "pizza"
        self.sample_machine = HuffmanMachine(target_string=self.sample_input)


    def test_frequency_sort(self):
        """
        Runs the frequency sort function in HuffmanMachine to assure it is
        creating a good frequency table of characters
        """
        node_array = []
        self.assertEqual(node_array, self.sample_machine.alpha_array)

    def test_build_node_tree(self):
        pass


    def test_encode_message(self):
        pass


    def test_decode_message(self):
        pass



if __name__ == '__main__':
    unittest.main()


