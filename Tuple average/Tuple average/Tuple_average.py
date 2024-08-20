import pandas as pd
import numpy as np
from sklearn import *

def TupleAVGToList(Tuplle):
    List = list(Tuplle)
    newList = [];
    x = 0
    y = 0
    for i in range(len(List)):
        for j in range(len(List)):
            x = x + List[j][i]
            y = y + 1
        newList.append(x/y)
        x = 0
        y = 0
    return newList

Tuple1 = ((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
List = TupleAVGToList(Tuple1)
print(List)