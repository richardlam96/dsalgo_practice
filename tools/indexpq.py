# INDEX PQ ###################################################################
# The IndexPQ uses the same idea of HeapPQ in swimming after every insert
# and sinking after every removal of the max to maintain a heapified binary
# tree of values.
# The main difference is in the way the values in the priority queue are
# accessed. IndexPQ uses parallel arrays, one to sort keys, another to store
# values related to those keys. Swimming and sinking only occur in the array
# of keys, and not in the values. Therefore, the array of values will at
# times be discontinuous, but this will allow changes to specific keys. Also,
# this implementation assumes N, the number of total records is known, hence,
# why the resize() function is not done.
#
# NOTE: for this implementation, as of now, there are no checks.
# If insert is used on an existing key, it will override the value with the
# change() function.
#

class IndexPQ(object):

    def __init__(self, N=10):
        self.qkeys = [None] * N
        self.pq = [None] * N
        self.qcapacity = N
        self.qsize = 0             # keep track of number of records


    def __swim(self):
        # compare with values in pq, but only change order of keys in
        # qkeys
        for i in reversed(range(self.qsize)):
            if (i // 2) >= 0:
                if self.pq[self.qkeys[i]] > self.pq[self.qkeys[i // 2]]:
                    temp = self.qkeys[i]
                    self.qkeys[i] = self.qkeys[i // 2]
                    self.qkeys[i // 2] = temp


    def __sink(self):
        for i in range(self.qsize):
            if (2*i + 1) < self.qsize:
                if self.pq[self.qkeys[i]] < self.pq[self.qkeys[2*i]]:
                    temp = self.qkeys[i]
                    self.qkeys[i] = self.qkeys[2*i]
                    self.qkeys[2*i] = temp
                if self.pq[self.qkeys[i]] < self.pq[self.qkeys[2*i + 1]]:
                    temp = self.qkeys[i]
                    self.qkeys[i] = self.qkeys[2*i + 1]
                    self.qkeys[2*i + 1] = temp


    def __resize(self):
        pass


    def insert(self, key, value):
        # insert or change value depending if preexistent
        # assume N does not need to be resized
        if not self.contains(key):
            self.qkeys[self.qsize] = key
            self.pq[key] = value
            self.qsize += 1
        else:
            self.change(key, value)

        self.__swim()


    def change(self, key, value):
        self.pq[key] = value

        self.__swim()


    def contains(self, key):
        return True if self.pq[key] else False


    def max_value(self):
        return self.pq[self.qkeys[0]]


    def max_index(self):
        return self.qkeys[0]


    def del_max(self):
        self.pq[self.qkeys[0]] = None                  # delete the value
        self.qkeys[0] = self.qkeys[self.qsize - 1]     # swap keys
        self.qkeys[self.qsize - 1] = None              # delete the last key
        self.qsize -= 1
        self.__sink()


    def empty(self):
        return False if self.qsize > 0 else True


    def size(self):
        return self.qsize


    # FOR TESTING PURPOSES ONLY !
    def show_keys(self):
        print("keys: ", self.qkeys)

    def show_pq(self):
        print("pq  : ", self.pq)

    def show_sorted_pq(self):
        for i in range(self.qsize):
            print(self.pq[self.qkeys[i]], end=" ")
        print()
