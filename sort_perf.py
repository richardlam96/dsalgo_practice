import time
# import matplotlib as mpl
# mpl.use('Agg')
# from matplotlib import pyplot

from numpy import random
# from functools import partial

from tools.sorts import shell_sort, quick_sort, heap_sort


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
def get_runtime(data, sorter):
    start_time = time.time()
    sorter(data)
    return time.time() - start_time


def main():
    algos = [sorted, shell_sort, quick_sort, heap_sort]
    # runtimes = []
    # larger samples to compare time
    doublingN = [500*2**n for n in range(0, 4)]
    for algo in algos:
        print("\n\n\n{} in milliseconds: ".format(algo.__name__.upper()))
        for N in doublingN:
            print("\nfor {}:".format(N))
            target = [i for i in range(N)]
            # print out three data points for each trial of size N
            for _ in range(3):
                runtime = get_runtime(target, algo) * 1000
                print("{:.5f}".format(runtime),
                        end=" ")
                # runtimes.append(runtime)
        print("\n")

#    # need to decide what and how data should be displayed
#    # maybe find average of values greater than zero and scatter or bar
#    # or learn histograms
#    plt.plot(doublingN, runtimes, label=algo.__name__)
#
#
#
#    # note: plot by sample size on x axis
#    plt.xticks(doublingN, doublingN)
#    plt.legend(loc=9)
#    plt.show()




if __name__ == "__main__":
    main()
