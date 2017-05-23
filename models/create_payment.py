import sqlite3

class Payment():
	'''
	Purpose: The Payment Class allows a customer to create a payment type.
	Properties:
		payment_type,
		account_number,
		customer FK to Customer
	'''

	def __init__(self, payment_type, account_number, customer):
		self.payment_type = payment_type
		self.account_number = account_number
		self.customer = customer

	def get_credit_card_name(self):
		return self.credit_card_name

	def get_account_number(self):
		return self.account_number


	def save(self, payment):

		# Refactor - move db info into its own file
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM Payment")
				payments = cursor.fetchall()

			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Payment`
					(
					payment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					payment_type TEXT NOT NULL,
					account_number TEXT NOT NULL,
					customer_id TEXT NOT NULL,
					FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
					)
				""")

			cursor.execute("""
				INSERT INTO Payment VALUES (null, "{}", "{}", "{}")
				""".format(
							payment.payment_type,
							payment.account_number,
							payment.customer
					)
				)

	def get_payments(customer):

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM Payment WHERE customer_id = {}".format(customer))
				payments = cursor.fetchall()
				return payments

			except (sqlite3.OperationalError) as err:
				print(err)
