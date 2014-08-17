import unittest
import median2

class TestMedian2(unittest.TestCase):
	def setUp(self):
		pass

	def test_median2(self):
		self.assertEqual(median2.median2(4,5,6), 5)

	def test_median2_other(self):
		self.assertEqual(median2.median2(3,3,4), 3)

if __name__ == '__main__':
	unittest.main()