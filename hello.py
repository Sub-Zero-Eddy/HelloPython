
# string concatenation

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
city = input("Enter City: ")
state = input("Enter State: ")
zip_code = input("Enter Zip Code: ")

# My name is first_name, last_name and I live in city, state zip_code

#message = "My name is " + first_name + ", " + last_name + " and I live in " + city + ", " + state + " " + zip_code

message = "My name is {0},{1} and I live in {2}, {3} {4}".format(first_name,last_name,city,state,zip_code)

print(message)











#snake case = first_number
#camel case = firstNumber

# input function always returns a String data type

a = 10 # integer
b = "hello" # string
c = 10.45 # float
d = True # boolean

# convert the input from String to Int
#first_number = float(input("Enter first number: "))
#second_number = float(input("Enter second number: "))

#first_number_as_int = int(first_number)
#second_number_as_int = int(second_number)
#print(first_number_as_int + second_number_as_int)

#result = first_number + second_number

#result = int(first_number) + int(second_number)
#print(result)
#number = int("45")

#first_number_as_int = int("45")
#second_number_as_int = int("70")

#some_result = first_number_as_int + second_number_as_int
#print(some_result)

#print(result)

#name = input("Enter your name: ")

#print(name)


#name = "John"
#age = 20
#version = 3.45

# print will print the value of name variable to the screen
#print(name)

#name = "Mary"

#print(name)
