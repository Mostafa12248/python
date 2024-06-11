#import files
import math
import random2

#function to take numbers and operation
def CalcFunction(num1 , num2 , operation) :
    if (operation == "+") :
        return num1 + num2 
    
    elif (operation == "-") :
        return num1 - num2 
    
    elif (operation == "*") :
        return num1 * num2 
    
    elif (operation == "/") :
        return num1 / num2 
    
    elif (operation == "pow") :
        return math.pow(num1 , num2) 
    
    elif (operation == "sqr") :
        return math.sqrt(num1)

    elif (operation == "random") :
        return random2.randrange(num1 , num2) 
    
    else : 
        return("miss operation")

