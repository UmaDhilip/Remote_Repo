import unittest
from validate_insertDB import *

class TestRegexp(unittest.TestCase):

    def test_chk_inFile_exists(self):
        valid_file = "C:\\Users\\mahii\\Project\\Proj_Python\\input_regexp.txt"
        invalid_file = "C:\\Users\\mahii\\Project\\Proj_Python\\input_regexp1.txt"

        result = chk_inFile_exists(valid_file)
        self.assertEqual(result,0)

        result = chk_inFile_exists(invalid_file)
        self.assertEqual(result, 1)

    def test_validate_email(self):
        valid_email="mahiister@gmail.com"
        invalid_email = " 11198989_asas*@gmai.com"

        result = validate_email(valid_email)
        self.assertEqual(result, True)

        result = validate_email(invalid_email)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()