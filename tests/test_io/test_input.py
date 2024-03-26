import unittest
import app.io.input as I

class TestInputFileReadFromStandardModule(unittest.TestCase):
    def test_read_file_builtin(self):
        """
        Test read_file_builtin
        """
        res = I.read_file_builtin("./tests/test_io/test_data/test.txt")
        self.assertEqual(res, "foo\nbar\n")

    def test_read_unexisting_file(self):
        """
        Test read_uneexistent_file
        """
        with self.assertRaises(FileNotFoundError):
           I.read_file_builtin("./tests/test_io/test_data/total.txt")

class TestInputFileReadFromPandasModule(unittest.TestCase):
    def test_read_file_pandas(self):
        """
        Test read_file_pandas
        """
        res = I.read_file_pandas("./tests/test_io/test_data/test.txt")
        self.assertEqual(res, ",foo\n0,bar\n")


    def test_read_pandas_unexisting_file(self):
        """
        Test read_uneexistent_file
        """
        with self.assertRaises(FileNotFoundError):
           I.read_file_pandas("./tests/test_io/test_data/total.txt")


