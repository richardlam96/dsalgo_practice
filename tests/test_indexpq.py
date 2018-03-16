import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from indexpq import IndexPQ
from numpy import random



def main():

    target = IndexPQ(20)
    input_data = [i for i in range(20)]
    random.shuffle(input_data)

    for i in range(10):
        target.insert(i, input_data[i])

    target.show_keys()
    target.show_pq()

    for i in range(5):
        print("remove:", target.max_value(), "at", target.max_index())
        target.del_max()

    for i in range(10, 15):
        target.insert(i, input_data[i])

    for i in range(10):
        print("remove:", target.max_value(), "at", target.max_index())
        target.del_max()

    target.show_keys()
    target.show_pq()


if __name__ == '__main__':
    main()
