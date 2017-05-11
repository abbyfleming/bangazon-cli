import os
import sys

sys.path.append("../")
from models.create_customer import Customer
from models.create_payment import Payment

class CLIPayment():
	"""
	"""

	def add_payment():
		'''Create a payment option'''

		# clear the screen
		os.system('cls' if os.name == 'nt' else 'clear')	
		
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
		os.system('cls' if os.name == 'nt' else 'clear')
