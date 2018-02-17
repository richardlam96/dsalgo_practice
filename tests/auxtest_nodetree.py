import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from nodetree import NodeTree


def main():

    # Initialize object object and samples here ###########################
    # Test Object:
    sample_tree = NodeTree()

    # Test Sample:
    sample_input = []
    for i in range(5):
        for _ in range(i):
            sample_input.append(i)
    # random.shuffle(target_sm)

    for value in sample_input:
        sample_tree.insert(value)


    # Begin testing functions here ###########################################
    # Initial View:
    print(sample_tree.get_array())




if __name__ == '__main__':
    main()
