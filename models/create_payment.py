import sqlite3

class Payment():
	'''
	Purpose: The Payment Class allows a customer to create a payment type.
	Properties:
		credit_card_name,
		account_number,
		customer FK to Customer
	'''

	def __init__(self, credit_card_name, account_number, customer):
		self.credit_card_name = credit_card_name
		self.account_number = account_number
		self.customer = customer

	def get_credit_card_name(self):
		return self.credit_card_name

	def get_account_number(self):
		return self.account_number


		
