import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

file = # '/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.BHmergers' #'/mnt/data0/jillian/h568/density1000/h568.cosmo75.4096gsHsbBH.BHmergers'   #'/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.BHmergers'    #'/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.BHmergers'
data= np.loadtxt(file)
print(data)
x = []
y = []

for i in ((len(data))/8):
    num = data[i,]


