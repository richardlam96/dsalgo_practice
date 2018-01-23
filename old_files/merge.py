def merge(target, lo, mid, hi):
    # first copy to auxilary array
    aux = []
    for i in range(lo, hi-lo+1):
        aux.append(target[i])

    # merge aux[lo:mid] to aux[mid+1:hi] back into target
    i = lo
    j = mid + 1
    for k in range(lo, hi-lo+1):
        if i > mid: 
            target[k] = aux[j]
            j += 1
        elif j > hi:
            target[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            target[k] = aux[j]
            j += 1
        else: # aux[i] <= aux[j]
            target[k] = aux[i]
            i += 1
    

# top down sort - recursively sorts arrays by sorting each half and 
#                 merging them
#
def td_sort(target):
    td_aux_sort(target, 0, len(target)-1) 

def td_aux_sort(target, lo, hi):
    if hi <= lo: return
    mid = lo + int((hi-lo)/2)
    td_aux_sort(target, lo, mid)
    td_aux_sort(target, mid+1, hi)
    merge(target, lo, mid, hi)


# bottom up sort 
# - nonrecursive, sorts arrays by sorting each pair,
#   then pair of pairs and so on
#
def bu_sort(target):
    N = target.size
    sizes = (2**i for i in range(0, N) if 2**i < N)
    for size in sizes:
        for lo in range(0, N-size, 2*size):
            merge(target, lo, lo+size-1, min(lo+2*size-1, N-1))
