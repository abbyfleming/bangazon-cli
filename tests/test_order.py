import unittest
import sys
sys.path.append("../")

from models.create_customer import Customer
from models.create_order import Order

class TestOrder(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.suzy = Customer(
			name = "Suzy Bishop",
			phone_number = "555-999-4444",
			address = "300 Summers End",
			city = "New Penzance",
			state = "Rhode Island",
			postal_code = "52801"
			)

		self.order = Order(self.suzy)



	def test_order_has_customer(self):
		self.assertEqual("Suzy Bishop", self.order.customer.name)

	def test_default_status_is_false(self):
		self.assertFalse(self.order.order_complete)


if __name__ == "__main__":
	unittest.main()