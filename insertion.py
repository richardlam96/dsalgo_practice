def sort(target):
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
        
                

