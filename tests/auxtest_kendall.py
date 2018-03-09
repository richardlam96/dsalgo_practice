import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from kendall_tau import kendall_tau


def main():

    a = [0,3,1,6,2,5,4]
    b = [0,3,1,6,4,2,5]
    print(kendall_tau(a,b))


if __name__ == '__main__':
    main()

