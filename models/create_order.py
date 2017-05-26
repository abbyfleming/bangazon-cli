import sqlite3

from models.create_customer import Customer

class Order():
	'''
	Purpose: The Order Class allows a customer to create an order.
	Properties:
		customer FK to Customer
		payment FK to Payment
	'''

	def __init__(self, customer):
		self.customer = customer
		self.payment = None
		self.order_complete = False



	def save(self, order):

		# Refactor - move db info into its own file
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				# Order is a SQL keyword
				cursor.execute("SELECT * FROM Invoice")
				orders = cursor.fetchall()
				

			except sqlite3.OperationalError:
				cursor.execute("""
				CREATE TABLE IF NOT EXISTS `Invoice`
					(
					invoice_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
					customer_id INTEGER NOT NULL,
					payment_id INTEGER NOT NULL,
					order_complete BOOLEAN NOT NULL,
					FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`),
					FOREIGN KEY(`payment_id`) REFERENCES `Payment`(`payment_id`)
					)
				""")


		# order.payment may need to be null	
		# order_id, customer_id, payment_id, active	
			cursor.execute("""
				INSERT INTO Invoice VALUES (null, "{}", "{}", "{}")
				""".format(
							order.customer,
							order.payment, 
							order.order_complete
					)
				)


	def get_active_order():
		customer = Customer.get_active_customer()

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT invoice_id FROM Invoice WHERE order_complete = 'False' AND customer_id = {}".format(customer))
				data = cursor.fetchone() #return only the invoice_id of the active order
				return data

			except (sqlite3.OperationalError) as err:
				pass # refactor?




	def complete_order(payment):
		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("UPDATE Invoice SET payment_id = {}, order_complete = 'True'".format(payment))

			except (sqlite3.OperationalError) as err:
				print(err)


			try:
				# set customer to inactive
				cursor.execute("UPDATE Customer SET active = 'False'")

			except (sqlite3.OperationalError) as err:
				print(err)