# for loop is used to complete the iteration or repeating the task
name=input("Enter your name: ")
# Iterate my name using for loop
# e.g. in c for(i=1; i<11; i++)
for i in name:
    print(i)

print("")
# print the no 1 to 10
for i in range(1,11):
    print(i)

print("")


for i in range(1,20):         #2 is step size   for i in range 
    if i%2 !=0:
        print("odd:")
    else:
        print("Even numbers: ")
        print(i)    
