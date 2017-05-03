import unittest
import sys
sys.path.append("../")

from models.create_category import Category

class TestCategory(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.camping = Category(
			name = "Camping"
			)

	def test_category_has_name(self):
		self.assertEqual("Camping", self.camping.get_category_name())


if __name__ == "__main__":
	unittest.main()		

