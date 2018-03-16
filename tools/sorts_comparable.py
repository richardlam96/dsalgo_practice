
# from comparable import Comparable

from numpy import random


# QUICK SORT COMPARABLE ######################################################
# Rewriting the quick sort from the orginal sort 'library' to allow use of
# new Comparables class.
#
# Basically, all there is to do is:
# - replace all target array value comparisons (some are index comparisons)
# - pass the key string into the quick sort function and use it whenever
#   comparisons are made.
#

def exchange(target, i, j):
    temp = target[i]
    target[i] = target[j]
    target[j] = temp


def insertion_sort_by_index(target, lo, hi, key):
    """
    Insertion sort that references by key, only sorting subarrays.

    This is mainly used for optimization of other sorts when those sorts
    reach a subarray size of 15 or less.

    input: target array to sort
           lo - index to start sorting
           hi - index to end sorting

    output: no return. sorts array
    """
    for i in range(lo+1, hi+1):
        pivot = target[i]
        j = i
        while j - 1 >= 0:
            if target[j-1].greater_than(pivot, key):
                target[j] = target[j-1]
                j -= 1
            else:
                break
        target[j] = pivot


def partition(target, lo, hi, key):

    if lo == hi:
        if lo == 0:
            insertion_sort_by_index(target, lo, hi+1, key)
        else:
            insertion_sort_by_index(target, lo-1, hi, key)
        return

    if hi-lo+1 <= 15:
        insertion_sort_by_index(target, lo, hi, key)
        return

    pivot = target[lo]
    i = lo
    j = hi
    while i < j:
        while i < hi and target[i].less_than(pivot, key):
            i += 1
        while j > lo and not target[j].less_than(pivot, key):
            j -= 1
        if j <= i:
            break

        exchange(target, i, j)

    partition(target, lo, j, key)
    partition(target, j + 1, hi, key)


def quick_sort_comparable(target, key=None):
    """
    Quick sort that uses the same algorithm as the basic quick sort but uses
    the Comparable class to allow sorting things by key.

    input: array of Comparable objects
           a string key of the attribute to which to base the sort

    output: none
    """
    random.shuffle(target)
    partition(target, 0, len(target)-1, key)




