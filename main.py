from parse import outputing



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file = open('input.txt', 'r')
    text = read_file.read()
    read_file.close()

    write_file = open('input.txt.out', 'w')
    write_file.write(outputing(text))
    write_file.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
