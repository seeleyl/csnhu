#array of weekdays
weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


#get starting day of week
selectedDay = input("What day of the week are you selecting?\n")
#check for valid input
while not selectedDay in weekdays: 
	selectedDay = input("\nNot a valid input.\nWhat day of the week are you selecting?\n" +
		"(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)\n")

#get number of days in future to look
numberDays = input("How many days in the future would you like to check?\n")
#check for valid input
while not numberDays.isdigit() or (int(numberDays) < 0):
	numberDays = input("Please input a non-negative integer.\n" + 
		"How many days in the future would you like to check?\n")

#I had originally tried not using any variables at all and doing the math
#in the print statements -- that proved to actually be rather difficult
#to make sure everything was typecast correctly, especially when running
#commands in a Python environment was much more forgiving than running a
#Python script.  Adding the futureDayIndex makes the code much easier to
#follow along with what is going on.
futureDayIndex = (weekdays.index(selectedDay) + int(numberDays)) % 7

print("You selected " + (selectedDay) + ".")
print("You wanted to look " + str(numberDays) + " days into the future.")
print("In " + str(numberDays) + " days, it will be a " + weekdays[futureDayIndex] + ".")
print("In " + str(int(numberDays)+1) + " days, it will be a " + 
	weekdays[(futureDayIndex+1)%7] + ".")
print("In " + str(int(numberDays)+2) + " days, it will be a " + 
	weekdays[(futureDayIndex+2)%7] + ".")
if (futureDayIndex == 0):
	print("In " + str(int(numberDays)-1) + " days, it will be a Saturday.")
else:
	print("In " + str(int(numberDays)-1) + " days, it will be a " + weekdays[(futureDayIndex-1)%7] + ".")

