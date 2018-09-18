
# conditions

# == is used to compare lhs with rhs - equality operator
if(1 == 2):
    print("EQUAL")
    a = 10
    b = 10
    c = a + b
else:
    print("NOT EQUAL")



#else:
#    print("NOT EQUAL")



# functions or methods

# age variable defined
age = 20

def validate_age(age):

    age = 10 # brand new variable called age defined inside the validate_age function

    if(age >= 18):
        print("age is greater or equal to 18")
    elif(age < 13):
        print("age is less than 13")
    else:
        print("age is not greater than 18 and not less than thirteen")

validate_age(age)
age = 10

 # we are passing 20
print("The value of age is {0} ".format(age))

# 4
def evenOrOdd(number):

    if(number % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

evenOrOdd(7)

#make = "Honda" is the default value for make if make is not provided
def display_car_information(model, make = "Honda"):
    print("----------------------------")
    print("Make {0} - Model {1}".format(make,model))

def add(first_number, second_number):
    return first_number + second_number
    print("Hey what about me! ")

# function with no arguments
def greet():
    print("Hello")

# function with multiple arguments
def greet(name,age):
    print("Hello ," + name)

#display_car_information("Honda","Accord")

#explicity specify the name of the parameters
#display_car_information(model = "Accord", make = "Honda")

#display_car_information(model = "Accord", make = "Toyota")




#greet("John",32)

#result = add(2,3)
# print(add(2,3))
#print(result)

# this is not the correct order to pass the arguments
#greet(32,"John")


#def greetJohn():
#    print("Hello John!")

#def greetMary():
#    print("Hello Mary!")

#greetJohn()
#greetMary()
