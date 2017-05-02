import os
import sys

sys.path.append("../")
from models.create_customer import Customer

class CustomerCLI():
	"""
	document
	"""

	def add_customer():
		'''Create a customer account'''

		name = input('Enter customer name \n> ')
		address = input('Enter street address \n> ')
		city = input('Enter city \n> ')
		state = input('Enter state \n> ')
		postal_code = input('Enter postal code \n> ')
		phone = input('Enter phone number \n> ')

		# Create a new customer / Instatiate
		new_customer = Customer(name, address, city, state, postal_code, phone)
		print("*****new_customer*****", new_customer.name)

		# Save to db
		new_customer.save(new_customer)


		

	
		