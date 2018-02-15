import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from nodetree import NodeTree


def main():
    sample_tree = NodeTree()
    sample_input = [i for i in range(10)]

    # test insert function
    for value in sample_input:
        sample_tree.insert(value)

    print(sample_tree.get_array())

    sample_tree.remove(1)
    print(sample_tree.has(1))


if __name__ == '__main__':
    main()
