# KENDALL TAU DISTANCE #######################################################
# Compares two arrays of size N with numbers 0 to N-1 and returns the number
# of differently ordered pairs.
#

def exchange(target, i, j):
    temp = target[i]
    target[i] = target[j]
    target[j] = temp


def kendall_tau(reference, target):
    counter = 0
    for i in range(len(reference)):
        if reference[i] == target[i]:
            continue;
        while reference[i] != target[i]:
            if i == target[i]:
                exchange(target, i, len(target)-1)
            else:
                exchange(target, i, target[i])
        counter += 1
    return counter
