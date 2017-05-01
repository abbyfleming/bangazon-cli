import os
import sys

sys.path.append("../")

from models.create_customer import Customer

class Customer():
	"""
	document
	"""

	def add_customer():
		'''Create a customer account'''
		## format

		name = input('Enter customer name \n> ')
		address = input('Enter street address \n> ')
		city = input('Enter city \n> ')
		state = input('Enter state \n> ')
		postal_code = input('Enter postal code \n> ')
		phone = input('Enter phone number \n> ')

		## Take input and save to database
		

	
		