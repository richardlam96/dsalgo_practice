from tools.heappq import HeapPQ
from numpy import random


def main():
    tasklist = HeapPQ()
    tasks = [val for val in range(20)]
    random.shuffle(tasks)

    for task in tasks:
        tasklist.insert(task)
    tasklist.show_pq()
    for _ in range(20):
        print(tasklist.rmMax())

if __name__ == '__main__':
    main()
