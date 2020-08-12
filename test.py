# coding: utf-8

import numpy as np
import os
from numpy import array
import pylab as pl

dir(pl)

path=r"D:\codes\R\backup\3khz.csv"

f=open(path)

lines=f.readlines()
def get_data(lines):
    sizeArray=[]
    for line in lines:
        line=line.replace("\n","")
        line=int(line)
        sizeArray.append(line)
    return array(sizeArray)

def draw_hist(lengths):
    data=lengths
    bins=np.linspace(10000,max(data),500)
    pl.hist(data,bins)
    pl.xlabel('Number of >10000(ns)')
    pl.ylabel('Number of Occurance')
    pl.title('Frequency distribution of number of >10000(ns)')
    pl.show()


Lengths=get_data(lines)
draw_hist(Lengths)






