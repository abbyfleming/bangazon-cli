import sqlite3

class Order():
	'''
	Purpose: The Payment Class allows a customer to create a payment type.
	Properties:
		customer FK to Product
		customer FK to Customer
	'''

	def __init__(self, product, customer):
		self.__product = product
		self.__customer = customer

	def get_customer(self):
		return self.__customer.get_full_name()


		
