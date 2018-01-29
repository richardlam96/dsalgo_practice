# INDEX PQ ###################################################################

# Try inheriting Heap PQ as a parent later?
#
# Ideally, this should allow printing input from multiple streams into one
# output stream without needing a large array to read them all into first.


class IndexPQ(object):

    def __init__(self, N=10):
        self.qkeys = [None] * N
        self.pq = [None] * N
        self.qcapacity = N
        self.qsize = 0        # keep track of number of records


    def __swim(self):
        pass


    def __sink(self):
        pass


    def insert(self, key, value):
        # for now, if override, just override
        # and assume N does not need to change, adjust later
        if not self.pq[key]:
            self.qsize += 1
        self.pq[key] = value

        self.__swim()


    def change(self, key, value):
        self.pq[key] = value

        self.__swim()


    def contains(self, location):
        return True if self.pq[location] else False


    def max_value(self):
        return self.pq[self.qkeys[0]]


    def max_index(self):
        return self.qkeys[0]


    def del_max(self):
        self.pq[self.keys[0]] = self.pq[self.keys[-1]]
        self.pq[self.keys[-1]] = None
        self.qsize -= 1

        self.__sink()


    def empty(self):
        return False if self.qsize > 0 else True


    def size(self):
        return self.qsize



