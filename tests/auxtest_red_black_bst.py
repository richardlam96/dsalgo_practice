import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

from red_black_tree import RedBlackBST


def main():
    letters = 'searchxmpl'
    sample_bst = RedBlackBST()
    for letter in letters:
        sample_bst.put(letter, 1)
    print('root', sample_bst.root.key)
    print(sample_bst.get_keys())
    
    for letter in letters:
        sample_bst.delete_min()
        print('root', sample_bst.root.key)
        print(sample_bst.get_keys())
        print()


if __name__ == '__main__':
    main()
