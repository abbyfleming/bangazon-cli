import sqlite3

class Product():
	'''
	Purpose: The Product Class allows a customer to create a product.
	Properties:
		name
		description
		quantity
		category FK to Category
	'''

	def __init__(self, name, description, quantity, category):
		self.__name = name
		self.__description = description
		self.__quantity = quantity
		self.__category = category

	def get_product_name(self):
		return self.__name

	def get_product_description(self):
		return self.__description

	def get_product_quantity(self):
		return self.__quantity

	def get_product_category(self):
		return self.__category.get_category_name()


		
