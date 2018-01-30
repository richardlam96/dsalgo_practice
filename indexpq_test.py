from tools.indexpq import IndexPQ
from numpy import random



def main():

    target = IndexPQ(20)
    input_data = [i for i in range(20)]
    random.shuffle(input_data)

    # insert 20
    for i in range(20):
        target.insert(i, input_data[i])

    target.show_keys()
    target.show_pq()

    for i in range(20):
        print("remove:", target.max_value(), "at", target.max_index())
        target.del_max()


if __name__ == '__main__':
    main()
