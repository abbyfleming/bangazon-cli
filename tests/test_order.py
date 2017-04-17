import unittest
import sys
sys.path.append("../")

from models.create_customer import Customer
from models.create_order import Order

class TestOrder(unittest.TestCase):

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
		

if __name__ == "__main__":
	unittest.main()