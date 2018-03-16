import unittest

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from comparable import Comparable
from transaction import Transaction



class ComparableBaseTest(unittest.TestCase):

    def setUp(self):
        self.comparables = []


    def test_basic_data_types(self):
        """
        Test that Comparable works with built-in data types.

        Builds Comparable objects with ordered integers and uses Comparable
        methods to assert that they are in the same order they were
        inserted.
        """
        for i in range(10):
            self.comparables.append(Comparable(i))

        for i in range(9):
            self.assertTrue(
                self.comparables[i].less_than(self.comparables[i+1]))


    def test_transaction_by_name(self):
        """
        Test Transaction class, which inherits from Comparable.

        Tests comparison of objects with more than one value attribute.
        """
        # also use this to check sorts later
        self.comparables.append(Transaction("whole foods", "2001-01-01", 200.00))
        self.comparables.append(Transaction("lotless", "2003-02-02",  40.00))
        self.comparables.append(Transaction("home depot", "2004-01-01", 100.00))
        self.comparables.append(Transaction("walmart", "2005-01-01", 150.00))
        self.comparables.append(Transaction("staples", "2007-01-01", 34.00))
        self.comparables.append(Transaction("rite aid", "2008-01-01", 20.00))
        self.comparables.append(Transaction("best buy", "2011-01-01", 20.00))

        # write more of these later. test all functions from Comparables with
        # each value in Transactions.
        self.assertFalse(
            self.comparables[0].less_than(self.comparables[1], "name"))

        self.assertTrue(
            self.comparables[0].less_than(self.comparables[1], "date"))

        self.assertTrue(
            self.comparables[0].greater_than(self.comparables[1], "amount"))

        self.assertTrue(
            self.comparables[5].equal_to(self.comparables[6], "amount"))











if __name__ == "__main__":
    unittest.main()
