import uuid
import math

class Student :
    #get number of method in the class
    number_of_methods = 0 
    def __init__(self , name , age , classes , id , degree) : 
        self.__name   = name
        self.__age    = age
        self.__classes = classes
        self.__id = id
        self.__degree = degree
        Student.number_of_methods +=1

#get student information
    def show_my_information(self) : 
        print(f"Name   :  {self.__name}")
        print(f"Age    :  {self.__age}")
        print(f"Class  :  {self.__classes}")
        print(f"ID     :  {self.__id}")
        print(f"Degree :  {self.__degree}")

    #test if student pass in exam or not
    def is_pass(self):
    #subjects name and degree
        subjects = {
        "English"  : 50, 
         "Arabic"   : 80,
         "Math"     : 120,
         "french"   : 40,
         "physics"  : 60,
         "chemistry": 60
        } 
        Total_degree = sum(subjects.values())

        # To calc degree 
        percentage = (self.__degree / Total_degree ) * 100

        if percentage == 100 :
            print("Appreciation :  Excellent")
            print(f"Percentage : {math.floor(percentage)}%")
            print("You Passed To Next Class")
        elif 80 <= percentage <= 95 :  
            print("Appreciation :  Very Good") 
            print(f"Percentage : {math.floor(percentage)}%")
            print("You Passed To Next Class")
        elif 60 <= percentage <= 79 :
            print("Appreciation :  Good")       
            print(f"Percentage : {math.floor(percentage)}%")
            print("You Passed To Next Class")
        elif 50 <= percentage <= 59 :
            print("Appreciation :  acceptable")   
            print(f"Percentage : {math.floor(percentage)}%")
            print("You Passed To Next Class")
        else : 
            print("Didn't Pass In Exam")   

#function to change your information 
    def Change_all_information(self , New_Name , New_Age , New_class , New_id) : 
        self.__name = New_Name 
        self.__age = New_Age
        self.__classes = New_class 
        self.__id = New_id
        
#function to change only name
    def change_name(self , name) :
        self.__name = name
#function to change only age
    def change_age(self , age) :
        self.__age = age
#function to change only id
    def change_id(self , id) :
        self.__id = id
#function to change only class
    def change_class(self , class1) :
        self.__classes = class1

#show full details and degree
    def show_degree(self) :
        self.show_my_information()
        self.is_pass()
        
