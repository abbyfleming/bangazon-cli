import os
import sys

sys.path.append('../')


def mainMenu():
	# clear the terminal
	os.system("clear")

	while True:

		print("\n""******************************************************* \n"
			"** Welcome to Bangazon! Command Line Ordering System ** \n"
			"******************************************************* \n")
		print("1. Create a customer account")
		print("2. Choose active customer")
		print("3. Create a payment option")
		print("4. Add product to shopping cart")
		print("5. Complete an order")
		print("6. See product popularity")
		print("7. Leave Bangazon!")

		try:
			choice = int(input(">"))

			if choice == 1: 
				print("*****add new customer*****")
			
			if choice == 2:
				print("*****choose active customer*****")	

			if choice == 3:
				print("*****create payment*****")

			if choice == 4:
				print("*****add product*****")

			if choice == 5:
				print("*****complete order*****")

			if choice == 6:
				print("*****see popularity*****")

			if choice == 7:
				print("*****EXIT******")
		
		except ValueError:
			print("*****oops*****")


		exit()

if __name__ == '__main__':
	# active_customer = session_manager.SessionManager()
	mainMenu()