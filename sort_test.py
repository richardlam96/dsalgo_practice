import time
# from matplotlib import pyplot as plt
from numpy import random
# from functools import partial

# from tools.comparable import Comparable
from tools.sorts import *



# move to sorts file to make it importable?
# or can you import from here?
def runtime(data, sorter):
    start_time = time.time()
    sorter(data)
    return time.time() - start_time



def main():

    algos = [sorted, insertion_sort, shell_sort, \
             # td_sort, bu_sort, \
             quick_sort # ,
             # quick_sort_med3,
             # quick_sort_3way #, \
             # swim_sink_sort
            ]


    # smaller sample to check validity
    # (except for python's sorted function)
    # NOTE: later use test functions to sort against sorted instead
    test_a = [5 for _ in range(5)]
    test_b = [4 for _ in range(4)]
    test_c = [i for i in range(15)]
    test = test_a + test_b + test_c
    print("ORIG:", test)
    print("ORIG:", sorted(test))

    for algo in algos[1:]:
        target = test[:]
        # random.shuffle(target)
        print("\n{}: ".format(algo.__name__))
        algo(target)
        print("{}: {}".format("GOOD" if target == sorted(test) else "BAD ",
                             target))

'''
    # larger samples to compare time
    doublingN = [500*2**n for n in range(0, 4)]
    for algo in algos:
        print("\n\n\n{} in milliseconds: ".format(algo.__name__.upper()))
        for N in doublingN:
            print("\nfor {}:".format(N))
            target = Comparable(N)
            # print out three data points for each trial of size N
            for _ in range(3):
                random.shuffle(target.data())
                print("{:.5f}".format(runtime(target.data(), algo)*1000),
                        end=" ")
    print("\n")

'''
    # need to decide what and how data should be displayed
    # maybe find average of values greater than zero and scatter or bar
    # or learn histograms
'''
        plt.plot(doublingN, runtimes, label=algo.__name__)



    # note: plot by sample size on x axis
    plt.xticks(doublingN, doublingN)
    plt.legend(loc=9)
    plt.show()

    for N in doublingN:
        target = Comparable(N)
        start_time = time.time()
        target.data().sort()
        print(time.time - start_time)

'''

if __name__ == "__main__":
    main()
