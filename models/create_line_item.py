import sqlite3

class LineItem():
	'''
	Purpose: The Order Class allows a customer to create a line item
	Properties:
		product FK to Product
		order FK to Order
	'''

	def __init__(self, order, product):
		self.order = order
		self.product = product
		
		

	def save(self, line_item):

			# Refactor - move db info into its own file
			with sqlite3.connect("bangazon_cli.db") as bang:
				cursor = bang.cursor()

				try:
					cursor.execute("SELECT * FROM LineItem")
					line_items = cursor.fetchall()

				except sqlite3.OperationalError:
					cursor.execute("""
					CREATE TABLE IF NOT EXISTS `LineItem`
						(
						line_item_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						order_id INTEGER NOT NULL,
						product_id INTEGER NOT NULL,
						FOREIGN KEY(`order_id`) REFERENCES `Order`(`order_id`),
						FOREIGN KEY(`product_id`) REFERENCES `Product`(`product_id`)
						)
					""")

				cursor.execute("""
					INSERT INTO LineItem VALUES (null, "{}", "{}")
					""".format(
								line_item.order,
								line_item.product	
						)
					)

	def get_line_items(invoice):

		with sqlite3.connect("bangazon_cli.db") as bang:
			cursor = bang.cursor()

			try:
				cursor.execute("SELECT * FROM LineItem WHERE order_id = {}".format(invoice))
				data = cursor.fetchall()
				return data

			except:
				pass