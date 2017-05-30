import unittest
import sys
sys.path.append("../")

from models.create_category import Category

class TestCategory(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.flowers = Category(
			name = "Flowers"
			)


	def test_category_has_name(self):
		self.assertEqual("Flowers", self.flowers.name)


if __name__ == "__main__":
	unittest.main()		

