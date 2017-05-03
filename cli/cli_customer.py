import os
import sys

sys.path.append("../")
from models.create_customer import Customer

class CLICustomer():
	"""
	The CLICustomer class is the CLI interface for adding a new customer. 
	After the customer information has been added, it will be saved to the db.
	The screen will then clear to show the main menu.
	"""

	def add_customer():
		'''Create a customer account'''

		# Refactor
		os.system('cls' if os.name == 'nt' else 'clear')

		name = input('Enter customer name \n> ')
		address = input('Enter street address \n> ')
		city = input('Enter city \n> ')
		state = input('Enter state \n> ')
		postal_code = input('Enter postal code \n> ')
		phone = input('Enter phone number \n> ')

		# Create a new customer / Instatiate
		new_customer = Customer(name, address, city, state, postal_code, phone)

		# Save to db
		new_customer.save(new_customer)

		# Refactor // Clear screen when finished to return to main menu
		os.system('cls' if os.name == 'nt' else 'clear')


		

	
		