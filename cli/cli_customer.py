import sys
import os


sys.path.append("../")
from models.create_customer import Customer

from styling import clear

class CLICustomer():
	"""
	The CLICustomer class is the CLI interface for adding a new customer. 
	After the customer information has been added, it will be saved to the db.
	The screen will then clear to show the main menu.
	"""
	def __init__(self):
	 	pass

	def add_customer(self):
		'''Create a customer account'''

		# Refactor
		clear()

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
		clear()


		

	
		