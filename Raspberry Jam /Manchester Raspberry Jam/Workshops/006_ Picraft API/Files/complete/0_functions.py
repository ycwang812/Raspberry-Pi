def triple(number_in):
	return number_in*3

def main():
	#user inputs a number
	number = int(input("Enter a number:"))
	
	#triple the number
	number = triple(number)

	#print the result
	print(number)
	
if __name__ == "__main__":
	main()
