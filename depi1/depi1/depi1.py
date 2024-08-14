import pandas as p
import numpy as n

for i in range (1,100):
    if (i >= 3 and i % 3 == 0 and i % 5 != 0):
       print("Fizz")
    elif(i >= 5 and i % 5 == 0 and i % 3 != 0):
        print("Buzz")
    elif (i >= 5 and i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
    else:
        print(i);    