import unittest

from numpy import random

from tools.sorts import insertion_sort, shell_sort, \
                        td_sort, bu_sort, \
                        quick_sort, quick_sort_avg2



algos = [insertion_sort, shell_sort, \
                  td_sort, bu_sort, \
                  quick_sort, quick_sort_avg2]


class TestSortingAlgosWithDuplicates(unittest.TestCase):

    def setUp(self):
        self.targets_no_dups = [[i for i in range(n)]
                                for n in range(10, 40, 10)]

    def test_algorithm(self):
        for target in self.targets_no_dups:
            for algo in algos:
                test = target[:]
                random.shuffle(test)
                algo(test)
                self.assertEqual(target, test)



class TestSortingAlgosWithoutDuplicates(unittest.TestCase):

    def setUp(self):
        # single target array to use
        self.target_yes_dups = []
        for n in range(12):
             self.target_yes_dups += [n for _ in range(n)]

    def test_algorithm(self):
        test = self.target_yes_dups[:]
        for algo in algos:
            random.shuffle(test)
            algo(test)
            self.assertEqual(test, self.target_yes_dups)



unittest.main()
