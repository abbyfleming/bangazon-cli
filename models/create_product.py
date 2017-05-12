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

	def __init__(self, name, description, price, quantity, category):
		self.name = name
		self.description = description
		self.price = price
		self.quantity = quantity
		self.category = category

	def get_product_name(self):
		return self.name

	def get_product_description(self):
		return self.description

	def get_product_quantity(self):
		return self.quantity



		
