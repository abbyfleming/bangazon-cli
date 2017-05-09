import os
import sys

sys.path.append("../")
from models.create_customer import Customer

class CLISelectCustomer():
	"""
	The CLISelectCustomer class is the CLI interface for selecting a customer
	to be active. Error handling will take care of selecting a valid customer
	and the active status will be changed in the database. Once complete, the
	user will return to the main menu.
	"""

	def choose_active():
		'''Choose active customer'''

		#clear the screen - refactor
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Which customer will be active?")

		# TODO: refactor customer display into own function
		customers = Customer.get_all_customers()

		for index, customer in enumerate(customers, start=1):
			print("{}. {}".format(index, customer[1]))

		# select a customer (input)
		selection = int(input('\n> '))

		# error handling
		if (selection > 0) and (selection < len(customers)):
			# change active to true
			active = Customer.active_customer(selection)
			
			# return to menu
			os.system('cls' if os.name == 'nt' else 'clear')
		
		else:
			print("ERROR.")
			# print the menu again





		