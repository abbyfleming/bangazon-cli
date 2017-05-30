import unittest
import sys
sys.path.append("../")

from models.create_customer import Customer

class TestCustomer(unittest.TestCase):

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

	
	def test_customer_has_name(self):
		self.assertEqual("Suzy Bishop", self.suzy.name)

	def test_customer_has_phone_number(self):
		self.assertEqual("555-999-4444", self.suzy.phone_number)

	def test_customer_default_active_status(self):
		self.assertFalse(self.suzy.active)



if __name__ == "__main__":
	unittest.main()