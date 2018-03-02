import sys 
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from numpy import random
from sorts import heap_sort


def main():
    algos = [heap_sort]
    # smaller sample to check validity
    # (except for python's sorted function)
    # NOTE: later use test functions to sort against sorted instead

    # test = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,6,6,6,6,6,6,66]
    test = [i for i in range(20)]
    print("ORIG:", test)
    print("ORIG:", sorted(test))

    for algo in algos:
        target = test[:]
        print("\n{}: ".format(algo.__name__))
        random.shuffle(target)
        print("ORIG:", target)
        algo(target)
        print("{}: {}".format("GOOD" if target == sorted(test) else "BAD ",
                             target))



if __name__ == '__main__':
    main()
