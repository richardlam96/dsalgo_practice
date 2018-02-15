import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from numpy import random

from sorts import insertion_sort, shell_sort, \
                  td_sort, bu_sort, \
                  quick_sort, quick_sort_avg2, quick_sort_3way



algos = [insertion_sort, shell_sort, \
         td_sort, bu_sort, \
         quick_sort, quick_sort_avg2, quick_sort_3way]


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.targets_no_dups = [[i for i in range(n)]
                                for n in range(10, 40, 10)]

        self.targets_yes_dups = []
        for i in range(6, 12, 2):
            sample = []
            for j in range(i):
                 sample += [j for _ in range(j)]
            self.targets_yes_dups.append(sample)

    """
    Basic testing functions written in a very modular way to allow
    flexibility and future changes
    """
    def pair(self, target, algo):
        test = target[:]
        random.shuffle(test)
        algo(test)
        return test


    def no_dups_sample(self, algo):
        for target in self.targets_no_dups:
            test = self.pair(target, algo)
            self.assertEqual(test, target)


    def yes_dups_sample(self, algo):
        for target in self.targets_yes_dups:
            test = self.pair(target, algo)
            self.assertEqual(test, target)


    def run_sample_cases(self, algo):
        self.no_dups_sample(algo)
        self.yes_dups_sample(algo)


    """Run testing function(s) for each sort"""
    def test_insertion_sort(self):
        self.run_sample_cases(insertion_sort)


    def test_shell_sort(self):
        self.run_sample_cases(shell_sort)


    def test_td_sort(self):
        self.run_sample_cases(td_sort)


    def test_bu_sort(self):
        self.run_sample_cases(bu_sort)


    def test_quick_sort(self):
        self.run_sample_cases(quick_sort)


    def test_quick_sort_avg2(self):
        self.run_sample_cases(quick_sort_avg2)


    def test_quick_sort_3way(self):
        self.run_sample_cases(quick_sort_3way)


if __name__ == '__main__':
    unittest.main()
