import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from stack import Stack



def main():

    test = Stack()

    push_n = 1000
    pop_m = 899

    int_test = [i for i in range(0, push_n)]
    for _, value in enumerate(int_test):
        test.push(value)
    test.show()

    for _ in range(0, pop_m):
        test.pop()
    test.show()



if __name__ == "__main__":
    main()
