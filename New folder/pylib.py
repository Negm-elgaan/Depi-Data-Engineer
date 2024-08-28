#import numpy as np
#import matplotlib as mpl
#import pandas as pd
def pow2(x):
    return x * x
def add(x,y):
    return x + y 
def sub(x,y):
    return x - y
def div(x,y):
    try:
        x/y
    except ZeroDivisionError:
        print("cannot divide by zer0!")
    else:
        return x / y
def mul(x,y):
    return x * y 