import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from styling import clear

class CLISelectCustomer():
	"""
	The CLISelectCustomer class is the CLI interface for selecting a customer
	to be active. Error handling will take care of selecting a valid customer
	and the active status will be changed in the database. Once complete, the
	user will return to the main menu.
	"""
	def __init__(self):
	 	pass

	def choose_active(self):
		'''Choose active customer'''

		clear()
		
		while True:
			print("Which customer will be active?")
			customers = Customer.get_all_customers()

			for index, customer in enumerate(customers, start=1):
				print("{}. {}".format(index, customer[1]))

			selection = int(input('\n> ')) # select a customer

			# basic error handling
			if (selection > 0) and (selection <= len(customers)):
				active = Customer.set_active_customer(selection) # change active to true
				break
			
			else:
				clear()
				print("Try again.")

			





		