# Unit test for Problem F2 - Cat multiple file


# IMPORTS
from solution import cat
from os import remove
import unittest


# main
class CatTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = "dummy_file.txt"
        dummy_file = open(self.filename, "w")
        dummy_file.write("you should see this")
        dummy_file.close()

    def test_cat_contents(self):
        self.assertEqual("you should see this", cat(self.filename))

    def tearDown(self):
        remove(self.filename)


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
