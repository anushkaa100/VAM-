# class - class is  a collection of objects and function 
# syntax - class<class name>
#          statement 
class Anushka:
    print("My name is Anushka")
    age = 19
    email = "anushka@123gmail.com"
    gender = "Female"
# object creation and calling
# syntax - object:Class = Class()
anushka:Anushka = Anushka()
print(anushka.age) 
print(anushka.email)
print(anushka.gender)
# create a class and function
class Student:
    name = "Ron"
    email = "ron@gmail.com"
    def findMyAge(this,cY,bY):
        ageInYear = cY-bY
        print(ageInYear)
    def monthlyPocketMoney(this,wM,mM):
        monthlyPocketMoney=wM*mM
        print(monthlyPocketMoney)
stu:Student = Student()
stu.findMyAge(2024,2004)
stu.monthlyPocketMoney(200,4)

class CAR:
    model = 2024
    gears = 7
    def topSpeed(this,gR):
        topspeed=gR*50
        print("the top speed of the car is :", topspeed)
model:CAR=CAR()
model.topSpeed(int(input("Enter the gear fron 1 to 7 to get to top speed :")))        











