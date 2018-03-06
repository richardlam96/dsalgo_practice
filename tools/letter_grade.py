# NOTE: letter comparisons are switched so 'A' is the largest
class LetterGrade(object):

    def __init__(self, letter=""):
        self.letter = letter[0]
        self.extent = letter[1] 
        self.order = ["-", " ", "+"]
        # self.order = ["+", " ", "-"]


    def __hash__(self):
        # this works for both hashes, it just allows it to be 
        # put into dict
        # but hash(etc) is more unique
        # return 1
        return hash(self.letter + self.extent)


    def __lt__(self, other):
        if self.letter == other.letter:
            return self.order.index(self.extent) < \
                   other.order.index(other.extent)
        else: 
            return self.letter > other.letter


    def __gt__(self, other):
        if self.letter == other.letter:
            return self.order.index(self.extent) > \
                   other.order.index(other.extent)
        else: 
            return self.letter < other.letter


    def __eq__(self, other):
        if self.letter == other.letter:
            return self.order.index(self.extent) == \
                   other.order.index(other.extent)
        else: 
            return self.letter == other.letter


