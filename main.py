from parse import outputing
import sys

if __name__ == '__main__':

    filename = sys.argv[1]
    read_file = open(filename, 'r')
    text = read_file.read()
    read_file.close()

    write_file = open(filename + '.out', 'w')
    write_file.write(outputing(text))
    write_file.close()

