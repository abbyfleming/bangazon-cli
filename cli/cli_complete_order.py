import os
import sys
import locale #https://docs.python.org/2/library/locale.html#locale.currency

sys.path.append("../")
from models.create_order import Order
from models.create_line_item import LineItem
from models.create_product import Product
from models.create_payment import Payment
from models.create_customer import Customer

from styling import clear


class CLICompleteOrder():
	"""
	"""
	def __init__(self):
	 	pass

	def display_payment(self):
		menu = []

		customer = Customer.get_active_customer()
		payments = Payment.get_payments(customer)

		# create a list of lists including the enumerated number at index 0
		for index, option in enumerate(payments, start=1):
			payment_list = list(option)
			payment_list.insert(0, index)	
			menu.append(payment_list)
		
		# print the menu
		for item in menu:
			print("{}. {}".format(item[0], item[2])) # index, card_name

		selection = int(input('\n> '))
		choice = menu[selection - 1][1] # payment_id

		print(choice)



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

			if input('(Y/N) > ').lower() != 'n':
				# show cards
				print("show cards")

				self.display_payment()

			else: 
				# show main menu
				clear()

		
		else:
			print("Please add some products to your order first. Press any key to return to main menu.")


