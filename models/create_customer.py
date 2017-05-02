import sqlite3


class Customer():
	'''
	Purpose: The Customer Class allows a new customer to be created.
	Properties:
		name
		address
		city
		postal_code
		phone_number
		active
	
	'''

	def __init__(self, name, address, city, state, postal_code, phone_number):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.postal_code = postal_code
		self.phone_number = phone_number
		self.active = False


	def save(self, customer):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM Customer")
				customers = cursor.fetchall()

			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Customer`
					(
					customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					city TEXT NOT NULL,
					state TEXT NOT NULL,
					postal_code TEXT NOT NULL,
					phone_number TEXT NOT NULL,
					active BOOLEAN NOT NULL
					)
				""")

			cursor.execute("""
				INSERT INTO Customer VALUES (null, "{}", "{}", "{}", "{}", "{}", "{}")
				""".format(
							customer.name,
							customer.city,
							customer.state,
							customer.postal_code,
							customer.phone_number,
							customer.active
					)
				)
