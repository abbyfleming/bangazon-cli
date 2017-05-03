import sqlite3

class Order():
	'''
	Purpose: The Payment Class allows a customer to create a payment type.
	Properties:
		customer FK to Product
		customer FK to Customer
	'''

	def __init__(self, product, customer):
		self.product = product
		self.customer = customer

	def get_customer(self):
		return self.customer.get_full_name()


		
