import unittest
from findFirstRepeatCharacter import findFirstRepeatCharacter

class TestFindFirstRepeatCharacter(unittest.TestCase):
	def test_empty_string(self):
	    try:
	        self.assertTrue(findFirstRepeatCharacter('') == 'No repeat characters found!')
	        return('test_empty_string ... Passed!')
	    except AssertionError as error:
	        return('test_empty_string ... Failed')

if __name__ == '__main__':
	unittest.main()