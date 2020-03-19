import sys
import os
from hashlib import md5
from getpass import getpass
import doodle7
import math

username_list = ""
password_list = ""
hash_username = ""
hash_password = ""
def register():

	username = input('Enter your username : ')
	if username == False:
		print("Enter a valid username\n")
		register()
	password = getpass('Enter your password : ')

	hash_username = md5(username.encode()).hexdigest()
	hash_password = md5(password.encode()).hexdigest()

	with open("usernames.txt","a+") as file:
		file.write(f"{username},{hash_username},{hash_password},")



	print("You have registered successfully.")
	
	opt = input("a. Go to Login Page\nb. Exit the program\n")
	if opt == 'a':
		login()
	elif opt =='b':
		sys.exit(0)
	else:
		print("Invalid choice")
		sys.exit(0)



def login():

	with open("usernames.txt","r") as file:
		d = file.read().split(",")
	#	print(len(d))

	
	count = 3
	while True:
		username_check = input('Enter your username : ')
		password_check = getpass('Enter your password : ')

		hash_username_check = md5(username_check.encode()).hexdigest()
		hash_password_check = md5(password_check.encode()).hexdigest()
		
#		print(hash_username)
#		print(hash_password)

		if count == 0:
			print("Too many failed attempts\nTry again later")
			sys.exit(0)
		
		flag = 0
		i = 0
		while i <= math.floor(len(d)-2)/3:

			if i > len(d)-2:
				print("Incorrect username or password\nYou have {} attempts left".format(str(count)))
				count -= 1


			if username_check == d[3*i]:
				pass

				if hash_password_check == d[3*i + 2]:
					
					print("User authentication successful !!!")
					doodle7.main(username_check)
		
				else:	
					i += 1
					if i > math.floor(len(d)-2)/3:
						print("Incorrect username or password\nYou have {} attempts left".format(str(count)))
						count -= 1				
					else:
						continue
			
			else:
				i += 1
				if i > math.floor(len(d)-2)/3:
					print("Incorrect username or password\nYou have {} attempts left".format(str(count)))
					count -= 1				
				else:
					continue

def main():
	print("Choose one of the following : ")
	choice = input("a. Login to the chatroom \nb. Register\n")

	if choice == 'a':
		login()
	elif choice == 'b':
		register()
	else:
		print("Invalid choice")
		sys.exit(0)

if __name__ == "__main__":
	main()
