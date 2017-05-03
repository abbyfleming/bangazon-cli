import sqlite3

class Category():
	'''
	Purpose: The Payment Class allows a customer to create a payment type.
	Properties:
		name
	'''

	def __init__(self, name):
		self.name = name

	def get_category_name(self):
		return self.name


		
