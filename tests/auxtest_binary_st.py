import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from binary_st import BinaryST



def main():
    sample_bst = BinaryST()

    # input five letter-number key-value pairs
    sample_bst.put("B", 2)
    sample_bst.put("A", 1)
    sample_bst.put("D", 4)
    sample_bst.put("E", 5)
    sample_bst.put("C", 3)


    # show the tree
    print("The tree:")
    sample_bst.print_tree()

    
    # check the size (which should be 5)
    print("Size:")
    if sample_bst.size() == 5:
        print("Success!")
    else:
        print("Nuuu! You got", sample_bst.size())

    # check the minimum value
    print("Min value:")
    print(sample_bst.min().key, sample_bst.min().value)

    # check the maximum value
    print("Max value:")
    print(sample_bst.max().key, sample_bst.max().value)

    # delete middle values
    sample_bst.delete("B")
    sample_bst.delete("C")
    sample_bst.delete("D")
    # get a list of keys
    
    keylist = sample_bst.get_keys("A", "E")
    print(keylist)

    # delete a value and check tree
    print("Delete min:")
    sample_bst.delete(sample_bst.min().key)   
    print("The tree:")
    sample_bst.print_tree()


if __name__ == '__main__':
    main()
