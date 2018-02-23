import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from transaction import Transaction

def main():
    print("Attempt to create two Transaction objects.")
    tx1 = Transaction("wholefoods")
    tx2 = Transaction("aldi")

    print("Attempt to compare two Transactions.")
    if tx1.less_than(tx2, "date"):
        print("less_than returned True")
    else:
        print("less_than returned False")




if __name__ == '__main__':
    main()
