import pandas as pd
import numpy as np
from sklearn import *

def TupleAVGToList(Tuplle):
    List = list(Tuplle)
    newList = [];
    x = 0
    y = 0
    for i in range(len(List[0])):
        for j in range(len(List)):
            x = x + List[j][i]
            y = y + 1
        newList.append(x/y)
        x = 0
        y = 0
    return newList


Tuple2 = ((1,1,-5),(30,-15,56),(81,-60,-39),(-10,2,3))
List2 = TupleAVGToList(Tuple2)
print(List2)
Tuple1 = ((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
List1 = TupleAVGToList(Tuple1)
print(List1)
