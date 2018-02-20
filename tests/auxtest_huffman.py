import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from huffman import HuffmanMachine


def main():

    sample_input = "cookies"
    sample_machine = HuffmanMachine(sample_input)

    # build the alpha array - works though has extra None object
    sample_machine.count_frequencies()
    sample_machine.sort_alpha()
    print(sample_machine.print_alpha())

    # building the node tree --- NOT being build correctly. repeating suffixes
    print("build node Tree")
    sample_machine.build_node_tree()
    sample_machine.print_tree(sample_machine.head)

    # build char_key dictionary
    print("character key")
    sample_machine.build_char_key()
    for char in sample_machine.char_key:
        print(char, sample_machine.char_key[char])

    # encode and decode --- should be fine
    print("encode and decode")
    encoded_message = sample_machine.encode()
    print(encoded_message)
    decoded_message = sample_machine.decode(encoded_message)
    print(decoded_message)


if  __name__ == '__main__':
    main()
