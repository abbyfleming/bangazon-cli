import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from models.create_payment import Payment
from models.create_product import Product
from models.create_order import Order
from models.create_line_item import LineItem

class CLIProduct():
	"""
	"""

	def add_product():
		'''Add product to shopping cart'''

		# clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')	
		
		# REFACTOR // error for TypeError
		# show a list of products
		products = Product.get_all_products() 

		for index, product in enumerate(products, start=1):
			print("{}. {}".format(index, product[1]))

		# last option should be 'Done adding products'
		finished = len(products) + 1
		print("{}. {}".format(finished, 'Done adding products'))		

		# error handling
		# ask user for input
		selection = int(input('\n> '))
		
		# is there an order for the customer?
		active = Order.get_active_order()

		# check to see if active returns None
		# refactor to try / except
		if active:
			print("yes, there's an active order")

			# get the product
			new_product = Product.get_product(selection)[0][0]
	
			# # add line order
			line_item = LineItem(active, new_product)
			line_item.save(line_item)


		else:
			# create the new order & add line item
			print("no, there's not an active order")

			# create new order
			customer = Customer.get_active_customer()
			new_order = Order(customer)
			new_order.save(new_order)
			active = Order.get_active_order()

			# get the product
			new_product = Product.get_product(selection)[0][0]

			# save line item
			line_item = LineItem(active, new_product)
			line_item.save(line_item)
		
		# finished? show main menu

