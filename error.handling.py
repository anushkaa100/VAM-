# try:
# print(x)
#error
# catch:
# type of error 

# print(x) -> name error
try:
    print(x)
except NameError:
    print("x not defined")

y=1/0
print(y)

try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("Zero division error")

# a="Anushka"
# b=int(a)  value error
# print(b)           
try:
    a="Anushka"
    b=int(a)
    print(b)
except:
    print("String not cast in int")

# import os   
#os.remove("myFile.txt") :File not found error     
import os
try:
    os.remove("myfile.txt")
except FileNotFoundError:
    print("file does not exist")

# myList=["Anushka","Harshita","Tanya"]
# print(myList[4]) index error
myList=["Anushka","Harshita","Tanya"]
try:
    print(myList[4])
except IndexError:
    print("Index out of range")

x=5
if x>5:  
    print(x)
else:
    print(x)
# x= 5
# try:
#   if x>5:
#   print(x) 
#   else:
#   print(x)
# except IndentationError:
    # print("Indentation Error")


# x = "Anushka" 
# y = 4
# c = x+y :- Type error
# print(c)
x = "Anushka"
y = 4
try:
    c=x+y
    print(c)
except TyprError:
    print("Concatenate only str") 
finally:              # The code in this will run even if there is error or not            
    print("Always run")

    






