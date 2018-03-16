
class Stack(object):

    def __init__(self, N=10):
        self.stack_array = [None] * N
        self.array_size = N
        self.data_size = 0

    def pop(self):
        if self.isEmpty():
            return ValueError
        else:
            if self.data_size < (self.array_size / 4) and self.array_size > 20:
                self.__resize(self.array_size // 2)
            stack_top = self.stack_array[self.data_size-1]
            self.stack_array[self.data_size-1] = None
            self.data_size -= 1
            return stack_top

    def __resize(self, new_size):
        temp_array = [None] * new_size
        for i in range(self.data_size):
            temp_array[i] = self.stack_array[i]
        self.stack_array = temp_array
        self.array_size = new_size

    def push(self, value):
        if self.data_size == self.array_size:
            self.__resize(2*self.array_size)
        self.data_size += 1 
        self.stack_array[self.data_size-1] = value

    def isEmpty(self):
        return True if self.data_size == 0 else False

    def size(self):
        return self.data_size

    # for testing purposes only
    def show(self):
        print(self.data_size, self.array_size)
