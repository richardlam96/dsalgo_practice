import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from symboltable import SymbolTable
from letter_grade import LetterGrade 

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.table = SymbolTable()
        self.table.put(LetterGrade("A+"), 4.33)
        self.table.put(LetterGrade("A "), 4.00)
        self.table.put(LetterGrade("A-"), 3.67)
        self.table.put(LetterGrade("B+"), 3.33)
        self.table.put(LetterGrade("B "), 3.00)
        self.table.put(LetterGrade("B-"), 2.67)
        self.table.put(LetterGrade("C+"), 2.33)
        self.table.put(LetterGrade("C "), 2.00)
        self.table.put(LetterGrade("C-"), 1.67)
        self.table.put(LetterGrade("D "), 1.00)
        self.table.put(LetterGrade("F "), 0.00)


    def test_table_content(self):
        pass


    def test_deletion(self):
        pass


    def test_insertion(self):
        pass


    def test_insert_then_delete(self):
        pass


    def test_delete_min(self):
        pass


    def test_delete_max(self):
        pass



