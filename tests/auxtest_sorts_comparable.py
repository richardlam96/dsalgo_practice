import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from transaction import Transaction
from sorts_comparable import insertion_sort_by_index, quick_sort_comparable

def main():

    # testing Comparable Sorts with Transaction objects
    testing_input = []
    testing_input.append(Transaction("whole foods", "2001-01-01", 200.00))
    testing_input.append(Transaction("lotless", "2003-02-02",  40.00))
    testing_input.append(Transaction("home depot", "2004-01-01", 100.00))
    testing_input.append(Transaction("walmart", "2005-01-01", 150.00))
    testing_input.append(Transaction("staples", "2007-01-01", 34.00))
    testing_input.append(Transaction("rite aid", "2008-01-01", 20.00))
    testing_input.append(Transaction("best buy", "2011-01-01", 20.00))

    # print(testing_input[0].less_than(testing_input[1]), "False")

    print("Quick Sort Comparable Test")
    quick_sort_comparable(testing_input)
    for obj in testing_input:
        obj.print_info()




if __name__ == '__main__':
    main()
