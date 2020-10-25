import hashlib #includes sha256 library
import getpass #hides typing password

shadow = {
	"admin":"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
	"ADMIN":"cbe6beb26479b568e5f15b50217c6c83c0ee051dc4e522b9840d8e291d6aaf46"
	}
#note: for testing purposes, user: admin password: password
#or user: ADMIN password: correcthorsebatterystaple

numberOfAttempts = 0

while numberOfAttempts < 3:
	getUserName = input("Enter username: \n")
	#hiding the password entered on the screen
	getPassword = getpass.getpass("Enter password: \n")

	#hashing the entered password
	getEncryptedPassword = hashlib.sha256(getPassword.encode())

	#ensuring plain-text password is removed from memory
	getPassword = "NotAPassword"

	#check if username matches, and if so, if hashes match
	if (getUserName) in shadow:
		if (shadow.get(getUserName) == getEncryptedPassword.hexdigest()):
			print("You have successfully logged in!\n")
			break

	print("You have " + str(2 - numberOfAttempts) + " attempts left!")
	numberOfAttempts += 1

	