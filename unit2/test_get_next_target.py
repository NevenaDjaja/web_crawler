import unittest
import get_next_target

class TestGetNextTarget(unittest.TestCase):
	def setUp(self):
		pass

	def test_get_next_target_s1(self):
		self.assertEqual(get_next_target.get_next_target('is a private institution of <a href="http://www.wikipedia.org/wiki/Higher_education"> higher education founded by'),('http://www.wikipedia.org/wiki/Higher_education', 83))

	def test_get_next_target_s2(self):
		self.assertEqual(get_next_target.get_next_target('good day'), (None, 0))

	def test_get_next_target_s3(self):
		self.assertEqual(get_next_target.get_next_target(''), (None, 0))

	def test_get_all_links_s1(self):
		self.assertEqual(get_next_target.get_all_links('<div id="top_bin"><div class="udacity float-left"><a href="http://udacity.com"></div><a href="http://google.com"></div>'), ['http://udacity.com', 'http://google.com'])

	def test_get_all_links_s2(self):
		self.assertEqual(get_next_target.get_all_links('http//xkcd.com'), [])


if __name__ == '__main__':
	unittest.main()