from numpy import random


# INSERTION SORT ##############################################################
# Insertion sort goes through each element in the array starting from the 
# second (index 1).  At the current index, it compares the current value with
# the value of the index right before it.  If that value is larger, move that
# value to the current index.
#
# The worse case: O(N^2), when the array is in reverse order
#

def insertion_sort(target):
    for i in range(1, len(target)):
        pivot = target[i]
        j = i
        while j - 1 >= 0:
            if target[j-1] > pivot:
                target[j] = target[j-1]
                j -= 1
            else:
                break;
        target[j] = pivot
    

# SHELL SORT ##################################################################
# Shell sort uses the same concept as insertion sort by moving values back
# if the values behind it are greater.  However, shell sort works faster by 
# analyzing all subsets of the array with elements taken from the array
# at intervals determined by (3*h) + 1 starting with h = 1. 
#
# The worst case: generally only a constant of merge sort, which has O(NlogN)
#

def shell_sort(target):
    N = len(target)
    gap = 1
    
    # get the increment sizes
    while gap < (N-1): gap = 3*gap +1

    while gap > 0:
        for i in range(gap, N):
            pivot = target[i]
            j = i
            while (j - gap) >= 0:
                if target[j - gap] > pivot:
                    target[j] = target[j - gap]
                    j -= gap
                else: 
                    break
            target[j] = pivot
        gap = (gap - 1) // 3


# MERGE SORTS #################################################################
# The merge() function that is used in both types of merge sort makes a copy 
# of a section of the target array with the indicies specified.  While keeping 
# track of the beginnings of the subarrays with indicies, merge compares the 
# values at the indices and inserts them back into the target array from 
# smallest to largest.
#
# Top down merge sort works up the tree by starting from the left side of
# every fork.
#
# Bottom up merge sort works up the tree by each level, starting from the 
# lowest level, pairing individual items, then pairing pairs, and so on.
#
# The worst case: O(NlogN).  Best performance with comparison sorts
# 
# NOTE about this implementation:
# This implementation does not use a class format, and this particularly
# matters because it is best to have a global aux array. But this 
# implementation passes around the aux a lot, which may slow it.

def merge(target, aux, lo, mid, hi):
     
    for i in range(lo, hi+1):
        aux[i] = target[i]

    # indicies for accessing aux
    i = 0
    mid = mid - lo
    j = mid + 1
    for k in range(lo, hi+1):
        if i > mid: 
            target[k] = aux[j]
            j += 1
        elif j > (hi-lo):
            target[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            target[k] = aux[i]
            i += 1
        else: # aux[i] >= aux[j]:
            target[k] = aux[j]
            j += 1

def td_sort(target):
    aux = [None] * len(target)
    td_aux_sort(target, aux, 0, len(target)-1) 

def td_aux_sort(target, aux, lo, hi):
    if hi <= lo: return
    if hi-lo+1 <= 15:
        insertion_sort(target[lo:hi+1])
        return
    mid = lo + (hi-lo)//2
    td_aux_sort(target, aux, lo, mid)
    td_aux_sort(target, aux, mid+1, hi)
    merge(target, aux, lo, mid, hi)


def bu_sort(target):
    N = target.size
    aux = [None] * N
    sizes = (2**i for i in range(0, N) if 2**i < N)
    for size in sizes:
        for lo in range(0, N-size, 2*size):
            merge(target, aux, lo, lo+size-1, min(lo+2*size-1, N-1))


# QUICK SORT ##################################################################
# There are two kinds of quick sort, one that will assume no knowledge of data
# and another that will assume that there are duplicate values in the data.
# In general, the quick sort chooses an element in the array as a 'pivot' and
# uses that to move the other elements either to the left, if it is less than
# the pivot, or to the right, if it is greater than the pivot.
# 

def partition(target, lo, hi):
    if lo == hi: 
        return

    if hi-lo+1 <= 15:
        insertion_sort(target[lo:hi+1]) 
        return

    pivot = target[lo]
    i = lo
    j = hi
    while i < j:
        while i < j and target[i] < pivot:
            i += 1
        while j > i and target[j] >= pivot:
            j -= 1
        if j > i:
            break
        elif j == i:    # already partitioned
            return
        temp = target[i]
        target[i] = target[j]
        target[j] = temp
        

    target[lo] = target[j]
    target[j] = pivot
    
    partition(target, 0, j)
    partition(target, j + 1, hi)

def quick_sort(target):
    random.shuffle(target)       # shuffle data to reduce bad partition
    partition(target, 0, len(target)-1)

def quick_sort_m3(target):
    pass
