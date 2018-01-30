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
        print(target.max_value())
        target.del_max()
        target.show_keys()
        target.show_pq()


if __name__ == '__main__':
    main()
