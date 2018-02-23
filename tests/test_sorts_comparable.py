import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from transaction import Transaction
from sorts_comparable import quick_sort_comparable


# It's really a Transaction Base Test
class ComparableSortsBaseTests(unittest.TestCase):

    def setUp(self):
        """
        Create a list of Transactions as well as lists of each type of value
        to compare to sample responses created in the test functions.
        """
        self.testing_input = []
        self.testing_input.append(Transaction("whole foods", "2001-01-01", 200.00))
        self.testing_input.append(Transaction("lotless", "2003-02-02",  40.00))
        self.testing_input.append(Transaction("home depot", "2004-01-01", 100.00))
        self.testing_input.append(Transaction("walmart", "2005-01-01", 150.00))
        self.testing_input.append(Transaction("staples", "2007-01-01", 34.00))
        self.testing_input.append(Transaction("rite aid", "2008-01-01", 20.00))
        self.testing_input.append(Transaction("best buy", "2011-01-01", 20.00))

        self.name_response = []
        self.date_response = []
        self.amount_response = []
        for obj in self.testing_input:
            self.name_response.append(obj.name)
            self.date_response.append(obj.date)
            self.amount_response.append(obj.amount)
        self.name_response.sort()
        self.date_response.sort()
        self.amount_response.sort()

    def get_sample_response(self, key):
        sample_response = []
        for obj in self.testing_input:
            sample_response.append(getattr(obj, key))

        return sample_response


    def test_default_compare_key(self):
        """
        Test using Comparable Sorts with the default key.
        """
        quick_sort_comparable(self.testing_input)
        self.assertEqual(self.name_response, self.get_sample_response("name"))


    def test_date_compare_key(self):
        """
        Test using Comparable Sorts with the date as the compare key.
        """
        quick_sort_comparable(self.testing_input, "date")
        self.assertEqual(self.date_response, self.get_sample_response("date"))


    def test_amount_compare_key(self):
        """
        Test using Comparable Sorts with the date as the compare key.
        """
        quick_sort_comparable(self.testing_input, "amount")
        self.assertEqual(self.amount_response, self.get_sample_response("amount"))




if __name__ == '__main__':
    unittest.main()
