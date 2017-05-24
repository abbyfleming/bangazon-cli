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
	

	# refactor / move customer into save new order
	def add_new_order_and_line_item(self, active, selection):
		customer = Customer.get_active_customer()
		new_order = Order(customer)
		new_order.save(new_order)

		active = Order.get_active_order()
		self.add_line_item(active, selection)


	def add_line_item(self, active, selection):
		# get the product
		new_product = Product.get_product(selection)[0][0]

		# add line order
		line_item = LineItem(active, new_product)
		line_item.save(line_item)


	
	# refactor / rename / break?
	def select_prduct(self, finished):
		while True:		
			selection = int(input('\n> '))	
			
			if selection == finished:
				break
			
			# refactor // if there is not an active order, create order in active order

			active = Order.get_active_order() # is there an active order?

			if active:
				print("yay, active order")
				self.add_line_item(active, selection)
			else:

				# basically replacing this logic
				print("yo, there's not an active order")
				self.add_new_order_and_line_item(active, selection)

		clear()

	
	
	def add_product(self):
		'''Add product to shopping cart'''

		clear()
		
		while True:

			# Refactor - move menu creation to own function
			products = Product.get_all_products() #show products

			for index, product in enumerate(products, start=1):
				print("{}. {}".format(index, product[1]))

			finished = len(products) + 1 # last option should be 'Done adding products'
			print("{}. {}".format(finished, 'Done adding products'))	

			self.select_prduct(finished)
			break # WHY? when the other loop ends, end this loop too?

		clear()


