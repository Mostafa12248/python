print("Calculate application")
#Take the inputs
num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))
#Take the operation
operation = input("Enter Your Operation : ")
# check the operation
if operation == "+" :
    print(num1+num2)

elif operation == "-" :
    print(num1-num2)    

elif operation == "*" :
    print(num1*num2)    

elif operation == "/" :
    print(num1/num2)    
# if i give it an not correct answer , it will be print this message
else : 
    print("Your Choice Is Not Correct")

#print this message in the end of process
print("Thanks For Using My Application")
