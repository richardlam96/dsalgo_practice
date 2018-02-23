import time
# from matplotlib import pyplot as plt
from numpy import random
# from functools import partial

# from tools.comparable import Comparable
from tools.sorts import quick_sort_3way


# NOTE: Need to rewrite this file to do what it actually was meant to do,
# which is to show the performance of the sort functions using matplotlib.
# Right now, it is just an auxillary test file to test specific sorts with
# specific inputs and should be very verbal.
#
# This file is really only used for quick_sort_3way, now that the other
# sorts are working fine, though none of them have been analyzed.
# There will be an overhaul of the sorting functions, which may only end up
# being one or two in a different file using Comparable objects and other
# objects that inherit from Comparable.
#
# So, the end product of this file, sort_perf, should use the old sorts module
# and some basic randomized integer lists to keep things simple and to keep
# the focus on the analysis of speed.
#

# move to sorts file to make it importable?
# or can you import from here?
def runtime(data, sorter):
    start_time = time.time()
    sorter(data)
    return time.time() - start_time



def main():

    algos = [quick_sort_3way]
    # smaller sample to check validity
    # (except for python's sorted function)
    # NOTE: later use test functions to sort against sorted instead
    #test_a = [5 for _ in range(5)]
    #test_b = [4 for _ in range(4)]
    #test_c = [i for i in range(15)]
    #test = test_a + test_b + test_c

    test = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,6,6,6,6,6,6,66]
    print("ORIG:", test)
    print("ORIG:", sorted(test))

    for algo in algos:
        target = test[:]
        print("\n{}: ".format(algo.__name__))
        random.shuffle(target)
        print(target)
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
