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
		self.__credit_card_name = credit_card_name
		self.__account_number = account_number
		self.__customer = customer

	def get_credit_card_name(self):
		return self.__credit_card_name

	def get_account_number(self):
		return self.__account_number

	def get_customer(self):
		return self.__customer.get_full_name()


		
