import os
import sys
from collections import OrderedDict

sys.path.append("../")
from cli_customer import CLICustomer
from cli_customer_active import CLISelectCustomer
from cli_payment import CLIPayment
from cli_product import CLIProduct

from styling import clear


def menu_loop():
	'''Show the menu'''
 
	clear() # clear the screen
	choice = None
 
	while choice != '7': # 7 is exit

		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))

		choice = input('> ').lower().strip()

		if choice in menu:
			menu[choice]()

#adding in the parenthesis instantiates with the init
# allowing self to be passed around
menu = OrderedDict([
	('1', CLICustomer().add_customer),
	('2', CLISelectCustomer().choose_active),
	('3', CLIPayment().add_payment),
	('4', CLIProduct().add_product) 
])

	
if __name__ == '__main__':
	menu_loop()

