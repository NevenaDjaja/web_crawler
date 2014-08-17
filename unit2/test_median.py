import unittest
import median

class TestMedian(unittest.TestCase):
	def setUp(self):
		pass

	def test_bigger(self):
		self.assertEqual(median.bigger(3,4), 4)

	def test_biggest(self):
		self.assertEqual(median.biggest(6,4,7), 7)

	def test_median(self):
		self.assertEqual(median.median(7,8,9), 8)

	def test_median2(self):
		self.assertEqual(median.median(1,2,2), 2)

	def test_median3(self):
		self.assertEqual(median.median(3,3,3), 3)

if __name__ == '__main__':
	unittest.main()

