import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from models.create_payment import Payment
from styling import clear

class CLIPayment():
	"""
	"""
	def __init__(self):
	 	pass

	def add_payment(self):
		'''Create a payment option'''

		# clear the screen
		clear()	
		
		# input (Enter payment type (e.g. AmEx, Visa, Checking))
		payment_type = input('Enter payment type (e.g. AmEx, Visa, Checking) \n> ')

		# input account number
		account_number = input('Enter account number \n')

		# get the active customer
		customer = Customer.get_active_customer()

		#save to database
		new_payment = Payment(payment_type, account_number, customer)
		new_payment.save(new_payment)

		# clear the screen / return to menu
		clear()
