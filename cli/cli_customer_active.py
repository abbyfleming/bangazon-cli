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

		#clear the screen - refactor
		clear()
		print("Which customer will be active?")

		# TODO: refactor customer display into own function
		customers = Customer.get_all_customers()

		for index, customer in enumerate(customers, start=1):
			print("{}. {}".format(index, customer[1]))

		# select a customer (input)
		selection = int(input('\n> '))

		# error handling
		if (selection > 0) or (selection < len(customers)):
			# change active to true
			active = Customer.set_active_customer(selection)
			
			# return to menu
			clear()
		
		else:
			print("ERROR.")
			# print the menu again





		