# Created by: John Hanekom
# Date: October 6th, 2022
# 
# This program asks for the users age, then declares what movie they can watch, and then restarts.
def main():
	age = int(input("Enter your age in years: "))
	if age >= 17:
		print("You can see a R rated movie alone")
		main()
	elif age >= 13:
		print("You can see a PG13 rated movie alone")
		main()
	else:
		print("You can see a G rated movie alone")
		main()
main()
