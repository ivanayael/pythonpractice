
number1 = int(input("Enter the first integer number: "))
number2 = int(input("Enter the second integer number: "))
number3 = int(input("Enter the third integer number: "))

#I suppouse that the first one is the largest one
largest_number = number1

if number2 > largest_number: largest_number = number2
elif number3 > largest_number: largest_number = number3

print("The largest number is ", int(largest_number))