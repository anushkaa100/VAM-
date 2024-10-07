# we have to use if else condition for decision making in python
# Check you are eligible for voting or not
# Get the age from user 
userAge=int(input("Enter your age: "))
# To check the user is eligible for voting, then check age must be greater than 18

if userAge > 18:
    print("You are eligible for voting ")
else:
    print("You're not eligible for voting ")





# Check the user is eligible for vote and suoer vote
# Supervote age should be greater than 55
# vote age should be greater than 18 less than 55
userAge=int(input("Enter your age: "))
if(userAge > 18 and userAge < 55):
    print("You are eligible for voting.")
elif(userAge > 55):
    print("You are eligible for super vote.")
else:
    print("You are not eligible for voting.")      


     
