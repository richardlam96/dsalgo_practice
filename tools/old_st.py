# ORDERED SYMBOL TREE ########################################################
# Symbol tree to store key and value pairs and allows clients to perform
# multiple functions.
#
# This implementation will use Python's dictionary data structure to make
# things easier and also to help you get more familiar with using it. So half
# of the functions will be simple, and the other half will need some thought.
#
# basic functions: put, get, delete, contains, is_empty, size, min, max
# other functions: floor, ceiling, rank, select, delete_min, delete_max,
#                  size(lo, hi), keys(lo, hi), keys
#

class SymbolTable(object):

    def __init__(self):
        self.table = {}


    def key_list(self):
        # for shorter code and a constantly updated list of keys
        # but easier to just update both lists when changes made?
        # but rank() and ceiling() functions may make this useless besides for
        # testing.
        return sorted(list(self.table.keys()))



    def put(self, new_key, new_val):
        self.table[new_key] = new_val


    def get(self, query_key):
        return self.table[query_key]


    def delete(self, query_key):
        if self.contains(query_key):
            del self.table[query_key]


    def contains(self, query_key):
        try:
            self.table[query_key]
            return True
        except KeyError:
            return False


    def is_empty(self):
        return bool(self.table)


    def size(self):
        return len(self.table)


    def min(self):
        return self.key_list()[0]


    def max(self):
        return self.key_list()[-1]


    def floor(self, query_key):
        target_index = self.key_list().index(query_key) - 1
        return self.key_list()[target_index]


    # rank() and ceiling() should be changed to use the binary search
    # approach.
    # then the rest of the functions should be based on rank()
    def ceiling(self, query_key):
        target_index = self.key_list().index(query_key) + 1
        return self.key_list()[target_index]


    def rank(self, query_key):
        i = 0;
        # return self.key_list().index(query_key) + 1


    def select(self, rank):
        return self.key_list()[rank-1]


    # for delete_min and delete_max, you can use delete(min()) as well
    # but this is also good for independency and checking
    def delete_min(self):
        del self.table[self.key_list().pop(0)]


    def delete_max(self):
        del self.table[self.key_list().pop()]


    def size(self, lo_key, hi_key):
        return self.key_list().index(hi_key) - self.key_list().index(lo_key)


    def keys(self, lo_key=None, hi_key=None):
        if not lo_key and not hi_key:
            return self.key_list()

        lo = self.key_list().index(lo_key)
        hi = self.key_list().index(hi_key)
        return self.key_list()[lo:hi+1]






