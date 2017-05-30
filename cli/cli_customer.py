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

		clear() 

		name = input('Enter customer name \n> ').strip()
		address = input('Enter street address \n> ').strip()
		city = input('Enter city \n> ').strip()
		state = input('Enter state \n> ').strip()
		postal_code = input('Enter postal code \n> ').strip()
		phone = input('Enter phone number \n> ').strip()

		# Create a new customer & instantiate
		new_customer = Customer(name, address, city, state, postal_code, phone)
		new_customer.save(new_customer)

		clear()


		

	
		