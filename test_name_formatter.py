import unittest
from name_formatter import name_formatter

class TesNameFormatter(unittest.TestCase):

    """ 
    Test case number 1
    """
    def test_name_formatter(self):
        res = name_formatter("javier mey")
        self.assertTrue(res, "Javier Mey")

if __name__ == '__main__':
    unittest.main()
