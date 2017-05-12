import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from models.create_payment import Payment
from models.create_product import Product

class CLIProduct():
	"""
	"""

	def add_product():
		'''Add product to shopping cart'''

		# clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')	
		
		# REFACTOR
		# show a list of products
		products = Product.get_all_products() 

		for index, product in enumerate(products, start=1):
			print("{}. {}".format(index, product[1]))

		# last option should be 'Done adding products'
		finished = len(products) + 1
		print("{}. {}".format(finished, 'Done adding products'))		

		# ask user for input
		selection = int(input('\n> '))

			# if !finished
				# save to database
				# show the product menu

			# else 
				# show main menu

