import unittest
from name_formatter import name_formatter

class NameFormatterTest(unittest.TestCase):
  def setUp(self):
    self.verificationErrors = []

  def tearDown(self):
    self.assertEqual([], self.verificationErrors)

  def test_init(self):
    try: self.assertEqual(name_formatter("javier mey"), "Javier Mey")
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual(name_formatter("DoyChin DoyCHev"), "Doychin Doychev")
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual(name_formatter("javier MEY"), "Javier Mey")
    except AssertionError as e: self.verificationErrors.append(str(e))
    try: self.assertEqual(name_formatter("JAVIER MEY"), "Javier Mey")
    except AssertionError as e: self.verificationErrors.append(str(e))

if __name__ == "__main__":
    unittest.main()
