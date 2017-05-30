import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from models.create_payment import Payment
from styling import clear

class CLIPayment():
	"""
	The CLIPayment class is the CLI interface for creating a payment type. 
	"""
	def __init__(self):
	 	pass

	def add_payment(self):
		'''Create a payment option'''

		clear()	# clear the screen
		
		payment_type = input('Enter payment type (e.g. AmEx, Visa, Checking) \n> ').strip()
		account_number = input('Enter account number \n').strip()

		# get the active customer
		customer = Customer.get_active_customer()

		#save to database
		new_payment = Payment(payment_type, account_number, customer)
		new_payment.save(new_payment)

		clear() # return to menu
