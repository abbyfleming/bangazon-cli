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




	def get_all_products():

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM Product WHERE quantity > 0")
				data = cursor.fetchall()
				return data
				
			except (sqlite3.OperationalError) as err:
				print(err)
		
	
	def get_product(product):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM Product WHERE product_id = {}".format(product))
				data = cursor.fetchall()
				return data

			except (sqlite3.OperationalError) as err:
				print(err)

