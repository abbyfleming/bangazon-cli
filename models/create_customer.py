import sqlite3


class Customer():
	'''
	Purpose: The Customer Class allows a new customer to be created.
	Properties:
		first_name
		last_name
		email
		phone_number
		address
		city
		zip_code
		active

	'''

	def __init__(self, first_name, last_name, email, phone_number, address, city, state, zip_code):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__email = email
		self.__phone_number = phone_number
		self.__address = address
		self.__city = city
		self.__state = state
		self.__zip_code = zip_code
		self.__active = False


	def get_full_name(self):
		return "{} {}".format(self.__first_name, self.__last_name)

	def get_email(self):
		return self.__email

	def get_phone_number(self):
		return self.__phone_number

	def get_full_address(self):
		return "{} {} {} {}".format(self.__address, self.__city, self.__state, self.__zip_code)

	def get_status(self):
		return self.__active


