import unittest

from parse import outputing


class TestMainFunctional(unittest.TestCase):
    def test1(self):
        read_file = open('tests/test1.txt', 'r')
        text = read_file.read()
        read_file.close()
        result = outputing(text)
        read_file = open('tests/out1.txt', 'r')
        right = read_file.read()
        read_file.close()

        self.assertEqual(result, right)

class TestSingleFunction(unittest.TestCase):
    def test2(self):
        read_file = open('tests/test2.txt', 'r')
        text = read_file.read()
        read_file.close()
        result = outputing(text)
        read_file = open('tests/out2.txt', 'r')
        right = read_file.read()
        read_file.close()

        self.assertEqual(result, right)

class TestElseBranch(unittest.TestCase):
    def test2(self):
        read_file = open('tests/test3.txt', 'r')
        text = read_file.read()
        read_file.close()
        result = outputing(text)
        read_file = open('tests/out3.txt', 'r')
        right = read_file.read()
        read_file.close()

        self.assertEqual(result, right)

class TestDegreeAndDenial(unittest.TestCase):
    def test2(self):
        read_file = open('tests/test6.txt', 'r')
        text = read_file.read()
        read_file.close()
        result = outputing(text)
        read_file = open('tests/out6.txt', 'r')
        right = read_file.read()
        read_file.close()

        self.assertEqual(result, right)


class TestConAndDis(unittest.TestCase):
    def test7(self):
        read_file = open('tests/test7.txt', 'r')
        text = read_file.read()
        read_file.close()
        result = outputing(text)
        read_file = open('tests/out7.txt', 'r')
        right = read_file.read()
        read_file.close()

        self.assertEqual(result, right)

if __name__ == '__main__':
    unittest.main()