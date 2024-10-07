# Typecasting convert one data type to another data type
price = 92.23
print(price)
print(type(price))

# convert to integer
payPrice = int(price)
print(payPrice)
print(type(payPrice))

# convert int into string
amount= 2300
stringAmount=str(amount)
print(stringAmount, "and data type is ", type(stringAmount))
print("")

# convert string into int
# gender = "female"
# genderIntoInt = int(gender)
# print(gender,"and data type is ", type(gender)) conversion not possible because string doesn't have an ascii number.
# print("")


# to take the input from user C language scanf
myName = input("Enter your name: ")
# input function has default return type as str.
myAge = input("Enter your age: ")
print("My name is ", myName , "and age is", myAge)
 
#  find the age in years. Then , born year and current year, given by user
currentYear = int(input("Enter the current year: "))
bornYear = int(input("Enter the born year: "))
age = currentYear - bornYear
print("The age is: ",age)





age=19
name="Anushka"
salary=45000

# show to pass the variables inside the print statement
# we have three ways to pass the variables to print statement
# print("My name is " + name +" and salary : "+ salary + "and age :"+age)

# solution 1: replace + by , when data type is not string
print("My name is",name ,"salary:",salary ,"and age:",age)

# solution 2: pass the variable in print statement with f{}
print(f"My name ia {name} salary: {salary} and age: {age}")
# solution 3: typecast the data into string 
salaryString = str(salary)
ageString = str(age)
print("Myn name is " + name + " salary: "+ salaryString + "and age: "+ ageString)

# to find the type of data we need tomuse type() function
print(type(name))
print(type(age))
print(type(salary))
print(type(name))
print(type(ageString))
print(name(salaryString))


# Currency converter Rupees to USD equal to 84
usd = int(input("Enter the currency in dollars: "))
rs=usd*84
print("USD = ",usd,"Rupees = ",rs)
print("")