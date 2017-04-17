import unittest
import sys
sys.path.append("../")

from models.create_customer import Customer

class TestCustomer(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.suzy = Customer(
			first_name = "Suzy",
			last_name = "Bishop",
			email = "s@s.com",
			phone_number = "555-999-4444",
			address = "300 Summers End",
			city = "New Penzance",
			state = "Rhode Island",
			zip_code = "52801"
			)

	
	def test_customer_has_full_name(self):
		self.assertEqual("Suzy Bishop", self.suzy.get_full_name())

	def test_customer_has_email(self):
		self.assertEqual("s@s.com", self.suzy.get_email())

	def test_customer_has_phone_number(self):
		self.assertEqual("555-999-4444", self.suzy.get_phone_number())

	def test_customer_has_address(self):
		self.assertEqual("300 Summers End New Penzance Rhode Island 52801", self.suzy.get_address())

	def test_customer_default_active_status(self):
		self.assertFalse(self.suzy.get_status())



if __name__ == "__main__":
	unittest.main()