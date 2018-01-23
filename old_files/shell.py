def interval(size):
    gap = 1
    while (3 * gap) + 1 < size:
        gap = (3 * gap) + 1

    return gap


def sort(target):
    gap = interval(len(target))
    while gap > 0:
        for i in range(2 * gap, len(target), gap):
            pivot = target[i]
            j = i
            while (j - gap) >= 0:
                if target[j - gap] > pivot:
                    target[j] = target[j - gap]
                    j -= gap
                else: 
                    break
            target[j] = pivot
        gap = int((gap - 1) / 3)
