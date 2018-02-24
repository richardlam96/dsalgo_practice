from numpy import random


def exchange(target, i, j):
    temp = target[i]
    target[i] = target[j]
    target[j] = temp

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
                break
        target[j] = pivot


def insertion_sort_by_index(target, lo, hi):
    """
    Insertion sort that references by key, only sorting subarrays.

    This is mainly used for optimization of other sorts when those sorts
    reach a subarray size of 15 or less. It really can be turned into the
    main insertion sort with some default arguments.

    Parameters:
    arg1: []     
        target array to sort
    arg2: int
        beginning index
    arg3: int
        ending index

    Return:
    no return 
        sorts array
    
    """
    for i in range(lo+1, hi+1):
        pivot = target[i]
        j = i
        while j - 1 >= 0:
            if target[j-1] > pivot:
                target[j] = target[j-1]
                j -= 1
            else:
                break
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
#

def merge(target, aux, lo, mid, hi):
    # copy values to aux
    for i in range(lo, hi+1):
        aux[i] = target[i]

    # aux will use the same indicies
    i = lo                              # beg of first subarray
    j = mid + 1                        # beg of second subarray
    for k in range(lo, hi+1):
        if i > mid:                    # left is exhausted
            target[k] = aux[j]
            j += 1
        elif j > hi:                   # right is exhausted
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
    if hi <= lo:
        return
    if hi-lo+1 <= 15:
        insertion_sort(target[lo:hi+1])
    mid = lo + (hi-lo)//2
    td_aux_sort(target, aux, lo, mid)
    td_aux_sort(target, aux, mid+1, hi)
    merge(target, aux, lo, mid, hi)


def bu_sort(target):
    N = len(target)
    aux = [None] * N
    sizes = (2**i for i in range(0, N) if 2**i < N)
    for size in sizes:
        for lo in range(0, N-size, 2*size):
            merge(target, aux, lo, lo+size-1, min(lo+2*size-1, N-1))


# QUICK SORT ##################################################################
# There are two kinds of quick sort, one that will assume no knowledge of data
# and another that will assume that there are duplicate values in the data.
#
# In general, the quick sort chooses an element in the array as a 'pivot' and
# uses that to move the other elements either to the left, if it is less than
# the pivot, or to the right, if it is greater than the pivot. This is shown
# in the first partition and quick_sort implementations. In the second set
# of implementations, the pivot uses the median of values at the first and
# last indicies, and gets rid of the need to make another exchange of values
#
# The second type of quick sort, quick_sort_3way, partitions the array
# into partitions of values equal to pivot, less than pivot, greater than
# pivot, and equal to pivot, respectively. It then reorganizes the array
# so all values equal to pivot are between those less than and greater than
# and then recursively sorts the less than and greater than partititons.
# In other words, this implementation is entropy optimal.
#
# NOTE: In the first implementation of the partition function, the values
# that are equal to the pivot need to be on the right becuase that
# partitioning scheme grabs values from the left. If values equal are
# placed on the left, sometimes, the algorithm will reach a point where it
# will indefinitely switch between two partitions of the same size but with
# different values at the beginning of the array. Also, the traveling i
# and j indicies need to cross each other to avoid a case where they
# are both pointing to the same value and having insertion_sort take over.
#
# In the second implementation of the partitioning function, it is it's own
# function because this implementation is not in the book. With avg2, after
# each partition, it splits again into subarrays from 0 to j-1 and j to hi,
# instead of from 0 to j and j+1 to hi. The reason for this is because
# the pivot is created using the first and last values in the array, which
# is why it keeps the equivalent values on the right, like the first
# implementation of partition as well. Perhaps this comes to show that this
# method of partitioning is not the best?
#
def partition(target, lo, hi):

    if lo == hi:
        if lo == 0:
            insertion_sort_by_index(target, lo, hi+1)
        else:
            insertion_sort_by_index(target, lo-1, hi)
        return

    if hi-lo+1 <= 15:
        insertion_sort_by_index(target, lo, hi)
        return

    pivot = target[lo]
    i = lo
    j = hi
    while i < j:
        while i < hi and target[i] < pivot:
            i += 1
        while j > lo and target[j] >= pivot:
            j -= 1
        if j <= i:
            break

        exchange(target, i, j)

    partition(target, lo, j)
    partition(target, j + 1, hi)


def quick_sort(target):
    random.shuffle(target)
    partition(target, 0, len(target)-1)



def partition_avg2(target, lo, hi):

    if lo == hi:
        if lo == 0:
            insertion_sort_by_index(target, lo, hi+1)
        else:
            insertion_sort_by_index(target, lo-1, hi)
        return

    if hi-lo+1 <= 15:
        insertion_sort_by_index(target, lo, hi)
        return

    pivot = (target[lo] + target[hi]) / 2
    i = lo
    j = hi
    while i < j:
        while i < j and target[i] < pivot:
            i += 1
        while j > i and target[j] >= pivot:
            j -= 1
        if j <= i:
            break

        temp = target[i]
        target[i] = target[j]
        target[j] = temp

    partition_avg2(target, 0, j-1)
    partition_avg2(target, j, hi)


def quick_sort_avg2(target):
    random.shuffle(target)
    partition_avg2(target, 0, len(target)-1)



def partition_3way(target, lo, hi):

    if lo == hi:
        if lo == 0:
            insertion_sort_by_index(target, lo, hi+1)
        else:
            insertion_sort_by_index(target, lo-1, hi)
        return

    # changed this to 3 for testing
    if hi-lo+1 <= 3:
        insertion_sort_by_index(target, lo, hi)
        return

    pivot = target[lo]
    p = lo + 1         # forward moving indicies
    i = p + 1           # p stays in switch pos, i moves
    q = hi              # backward moving indicies
    j = q - 1           # vice versa

    # sort so that values == pivot are on left and right
    # with values < and > pivot between, respectively
    while True:
        while i < hi:
            if target[i] == pivot:
                exchange(target, p, i)
                p += 1
                i += 1
            if target[i] < pivot:
                i += 1
            elif target[i] > pivot:
                break;
        while j > lo:
            if target[j] == pivot:
                exchange(target, q, j)
                q -= 1
                j -= 1
            if target[j] > pivot:
                j -= 1
            elif target[j] < pivot:
                break;

        if j <= i:
            break

        print("exch", target[i], target[j])
        print(target)
        exchange(target, i, j)
        print(target)

    print("rearrange")
    print(target[p:j+1], target[i:q+1])
    # switch values so that values equal to pivot are in the middle
    # first, from first index to j (last value smaller than pivot)
    k = lo
    for x in reversed(range(p, j+1)):
        exchange(target, k, x)
        k += 1
        if k < p: break

    k = hi
    for x in range(i, q+1):
        exchange(target, k, x)
        k -= 1
        if k > q: break

    print(target)

    partition_3way(target, lo, j-(lo-p))
    partition_3way(target, i+(hi-q), hi)


def quick_sort_3way(target):
    # random.shuffle(target)
    partition_3way(target, 0, len(target)-1)


# HEAPSORT ###################################################################
# Heap sort uses the sink function from HeapPQ and IndexPQ to sort an array
# in two phases: the heap construction and the sortdown
#

def swim(target):
    for i in reversed(range(len(target))):
        if (i // 2) >= 0:
            if target[i] > target[i // 2]:
                exchange(target, i, i // 2)


# def sink(target):
#     for i in range(len(target)):
#         if (2*i) < len(target) and target[i] < target[2*i]:
#             exchange(target, i, 2*i)
#         if (2*i + 1) < len(target) and target[i] < target[2*i + 1]:
#             exchange(target, i, 2*i+1)


def sink(target, lo, hi):
    for i in range(lo, hi):
        if (2*i) < len(target) and target[i] < target[2*i]:
            exchange(target, i, 2*i)
        if (2*i + 1) < len(target) and target[i] < target[2*i + 1]:
            exchange(target, i, 2*i+1)

def print_tree(target):
    i = 0
    while (2*i+1) < len(target):
        print(target[i])
        print("l", target[2*i], "r", target[2*i+1])
        i += 1


def swim_sink_sort(target):
    # heap construction
    N = len(target)
    for i in reversed(range(N//2)):
        sink(target, i, N)
    
    print_tree(target)
    print("mid", target)
    
    # break and resort
    while N > 1:
        exchange(target, 0, N-1)
        sink(target, 0, N-1)
        N -= 1

def heap_sort(target):
    pass
