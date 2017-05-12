import os
import sys
from collections import OrderedDict

sys.path.append("../")
from cli_customer import CLICustomer
from cli_customer_active import CLISelectCustomer
from cli_payment import CLIPayment
from cli_product import CLIProduct


def clear():
   os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
 '''Show the menu'''
 clear()
 choice = None
 
 # Refactor // Option 7 should be exit
 while choice != '7':
   
   for key, value in menu.items():
     print('{}) {}'.format(key, value.__doc__))
   
   choice = input('> ').lower().strip()
   
   if choice in menu:
     menu[choice]()
 

menu = OrderedDict([
  ('1', CLICustomer.add_customer),
  ('2', CLISelectCustomer.choose_active),
  ('3', CLIPayment.add_payment),
  ('4', CLIProduct.add_product)
])

     
if __name__ == '__main__':
      menu_loop()
     
