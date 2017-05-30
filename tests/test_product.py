# import unittest
# import sys
# sys.path.append("../")

# from models.create_category import Category
# from models.create_product import Product

# class TestProduct(unittest.TestCase):

# 	@classmethod
# 	def setUpClass(self):

# 		self.camping = Category(
# 			name = "Camping"
# 			)

# 		self.tent = Product(
# 			name = "Happy Camper Two Person Tent",
# 			description = "Small two person tent for hobbyists.",
# 			quantity = 10,
# 			category = self.camping
# 			)


# 	def test_product_has_name(self):
# 		self.assertEqual("Happy Camper Two Person Tent", self.tent.get_product_name())

# 	def test_product_has_description(self):
# 		self.assertEqual("Small two person tent for hobbyists.", self.tent.get_product_description())

# 	def test_product_has_quantity(self):
# 		self.assertEqual(10, self.tent.get_product_quantity())

# 	def test_product_has_category(self):
# 		self.assertEqual("Camping", self.tent.category.get_category_name())


# if __name__ == "__main__":
# 	unittest.main()		

