import sys 
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from symboltable import SymbolTable
from letter_grade import LetterGrade

def main():

    table = SymbolTable()
    
    table.put(LetterGrade("A+"), 4.33)
    table.put(LetterGrade("A "), 4.00)
    table.put(LetterGrade("A-"), 3.67)
    table.put(LetterGrade("B+"), 3.33)
    table.put(LetterGrade("B "), 3.00)
    table.put(LetterGrade("B-"), 2.67)
    table.put(LetterGrade("C+"), 2.33)
    table.put(LetterGrade("C "), 2.00)
    table.put(LetterGrade("C-"), 1.67)
    table.put(LetterGrade("D "), 1.00)
    table.put(LetterGrade("F "), 0.00)


    for key in table.key_list():
        print(key.letter + key.extent, table.get(key))



if __name__ == '__main__':
    main()
