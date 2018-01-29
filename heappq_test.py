from tools.heappq import HeapPQ
from numpy import random


def main():
    tasklist = HeapPQ()
    tasks = [val for val in range(30)]
    random.shuffle(tasks)

    # insert 10
    for task in tasks[:10]:
        try:
            tasklist.insert(task)
        except IndexError:
            print("IndexError: qsize {} qcap {}".format(tasklist.qsize,
                                                        tasklist.qcapacity))
            return
        print("--- inserted {} ---".format(task))

    # do and remove 3
    for _ in range(3):
        print("task done and removed: {}".format(tasklist.rmMax()))

    # insert 10
    for task in tasks[10:20]:
        tasklist.insert(task)
        print("--- inserted {} ---".format(task))

    # remove 10
    for _ in range(10):
        print("removed task {}".format(tasklist.rmMax()))

    # remove the rest
    while not tasklist.isEmpty():
        print("rest: {}".format(tasklist.rmMax()))

if __name__ == '__main__':
    main()
