import os
import sys
import locale #https://docs.python.org/2/library/locale.html#locale.currency

from styling import clear

sys.path.append("../")
from models.create_order import Order
from models.create_line_item import LineItem
from models.create_product import Product


class CLICompleteOrder():
	"""
	"""
	def __init__(self):
	 	pass

	def complete_order(self):
		'''Complete an order'''

		clear()
		active = Order.get_active_order() # is there an active order?

		if active:
			total = 0

			line_items = LineItem.get_line_items(active) # get line items of active order
			
			for product in line_items:
				product_id = product[2] #line_item_id, order_id, product_id
				price = Product.get_product(product_id)[0][3] #price

				total += price

			# display total
			locale.setlocale( locale.LC_ALL, '' )
			pretty_total = locale.currency(total, grouping=True )
			print("Your order total is {}. Ready to purchase?".format(pretty_total))

		
		else:
			print("Please add some products to your order first. Press any key to return to main menu.")
			# Display error message


