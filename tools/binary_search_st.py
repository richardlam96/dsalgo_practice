# ORDERED SYMBOL TREE ########################################################
# The non-lazy way, aka, the more raw way of doing it without using Python's
# dictionary data structure.
# Instead, here the underlying data structure is a pair of parallel arrays.
# And the most important function here is the rank() function.
#

class SymbolTable(object):

    def __init__(self):
        self.keys = []
        self.values = []


    def rank(self, query_key):
        """
        Finds the index of where query_key is stored.

        Return index if found, otherwise return None.
        """
        lo = 0
        hi = len(self.keys)
        while lo < hi:
            mid =  (lo + hi) // 2
            if self.keys[mid] < query_key:
                hi = mid - 1
            elif self.keys[mid] > query_key:
                lo = mid + 1
            else:
                return mid
        return lo


    def select(self, rank_index):
        return self.keys[rank_index]


    def put(self, new_key, new_value):
        """
        Checks if new_key exists. If it does, update value as needed.
        Otherwise, append it to the lists while maintaining order.
        """
        index = self.rank(new_key)

        if index < len(self.keys):
            if self.values[index] != new_value:
                self.values[index] = new_val
        else:
            self.keys.insert(index, new_key)
            self.values.insert(index, new_value)


    def get(self, query_key):
        index = self.rank(query_key)
        return self.keys[index]


    def delete(self, query_key):
        index = self.rank(query_key)
        return self.keys.pop(index)


    def contains(self, query_key):
        if self.rank(query_key):
            return True
        else:
            return False


    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True


    def size(self):
        return len(self.keys)


    def min(self):
        return self.keys[0]


    def max(self):
        return self.keys[-1]


    def delete_min(self):
        self.delete(self.min())


    def delete_max(self):
        self.delete(self.max())


    def keys(self, lo_key, hi_key):
        lo = self.rank(lo_key)
        hi = self.rank(hi_key)
        return self.keys[lo:hi+1]
