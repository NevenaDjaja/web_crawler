import unittest
import find_last

class TestFindLast(unittest.TestCase):
	def setUp(self):
		pass

	def test_find_last(self):
		self.assertEqual(find_last.find_last("find me if you find me yet","me"), 20)

	def test_find_last2(self):
		self.assertEqual(find_last.find_last("111111111", "1"), 8)

	def test_find_last3(self):
		self.assertEqual(find_last.find_last('aaaaa', 'aa'), 3)

if __name__ == '__main__':
	unittest.main()