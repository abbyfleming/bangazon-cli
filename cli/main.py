
from collections import OrderedDict
import os
import sys

sys.path.append("../")
from cli_customer import CLICustomer


def clear():
   os.system('cls' if os.name == 'nt' else 'clear')


def menu_loop():
 '''Show the menu'''
 clear()
 choice = None
 
 # Refactor // Option 7 should be exit
 while choice != 'q':
   print("Enter 'q' for quit.")
   for key, value in menu.items():
     print('{}) {}'.format(key, value.__doc__))
   
   choice = input('> ').lower().strip()
   
   if choice in menu:
     menu[choice]()
 

menu = OrderedDict([
  ('1', CLICustomer.add_customer),
])

     
if __name__ == '__main__':
      menu_loop()
     
