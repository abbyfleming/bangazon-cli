import unittest
import sys
sys.path.append("../")

from models.create_customer import Customer
from models.create_payment import Payment

class TestPayment(unittest.TestCase):

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

		self.card = Payment(
			credit_card_name = "Visa",
			account_number = "000 111 2222",
			customer = self.suzy
			)

	def test_card_has_customer(self):
		self.assertEqual("Suzy Bishop", self.card.get_customer())

	def test_card_has_name(self):
		self.assertEqual("Visa", self.card.get_credit_card_name())

	def test_card_has_account_number(self):
		self.assertEqual("000 111 2222", self.card.get_account_number())

