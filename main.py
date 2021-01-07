from parse import outputing


if __name__ == '__main__':

    while True:
        filename = input('Input name of file:')
        if filename.endswith(".txt"):
            read_file = open(filename, 'r')
            text = read_file.read()
            read_file.close()
            break
        else:
            print("It is not right file, repeat")

    write_file = open(filename + '.out', 'w')
    write_file.write(outputing(text))
    write_file.close()

