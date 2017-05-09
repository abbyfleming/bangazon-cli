import os
import sys

sys.path.append("../")
from models.create_customer import Customer

class CLISelectCustomer():
	"""
	documentation
	"""

	def choose_active():
		'''Choose active customer'''

		#clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Which customer will be active?")

		# display all customers
		customers = Customer.get_all_customers()

		for index, customer in enumerate(customers, start=1):
			print("{}. {}".format(index, customer[1]))

		# select a customer (input)
		active_customer = input('\n> ')

		# change active to true

		# return to menu