import os
import sys
sys.path.append("../")

from models.create_customer import Customer
from models.create_payment import Payment
from models.create_product import Product
from models.create_order import Order
from models.create_line_item import LineItem

from styling import clear


class CLIProduct():
	"""
	The CLISelectCustomer class is the CLI interface for adding a product to the invoice. If an order does not exsist for the customer, a new invoice will be created. Otherwise, the line items are added. Once complete (last option in menu), the user will be returned to the main menu.
	"""
	def __init__(self):
	 	pass
			
	
	def add_product(self):
		'''Add product to shopping cart'''

		clear()
		
		products = Product.get_all_products() #show products

		for index, product in enumerate(products, start=1):
			print("{}. {}".format(index, product[1]))

		finished = len(products) + 1 # last option should be 'Done adding products'
		print("{}. {}".format(finished, 'Done adding products'))

		selection = input('> ')

		new_product = Product.get_product(selection)[0][0]		
		active = Order.get_active_order() # is there an active order?
		print("*****active*****", active)

		if active is None:
			# create the order and fetch the id
			customer = Customer.get_active_customer() # create a new order
			new_order = Order(customer) # instantiate
			new_order.save(new_order) # save the order
			active = Order.get_active_order() # is there an active order?
			
			line_item = LineItem(active[0], new_product)
			line_item.save(line_item)

		else:
			line_item = LineItem(active[0], new_product)
			line_item.save(line_item)
			print("*****line_item saved*****")


