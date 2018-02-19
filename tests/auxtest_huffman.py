import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from huffman import HuffmanMachine


def main():

    sample_input = "ninja turtles love pizza."
    sample_machine = HuffmanMachine(sample_input)

    sample_machine.run()
    print(sample_machine.encode())



if  __name__ == '__main__':
    main()
