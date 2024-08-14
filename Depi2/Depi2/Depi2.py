from tokenize import String
import pandas as p
import numpy as n
def UserInfo():
    FirstName = input("Enter your first name:")
    LastName = input("Enter your last name:")
    Gender = input("Enter your gender:")
    while (Gender.lower() != "male" and Gender.lower != "female"):
        print("Invalid answer! please enter a valid answer")
        Gender = input("Enter your gender:")
    ID = 0 
    while (True):
        ID = input("Enter your Id:")
        try:
            ID = int(ID)
            break
        except ValueError:
            print("Invalid number! Please enter a valid number")
            
    Filename = "UserInfo.txt"
    File = open(Filename,"w")
    File.write(FirstName)
    File.write("#//#")
    File.write(LastName)
    File.write("#//#")
    File.write(Gender)
    File.write("#//#")
    File.write(str(id))
    File.close()
UserInfo()
        
    