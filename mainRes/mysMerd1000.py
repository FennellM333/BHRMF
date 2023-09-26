from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

file =  '/mnt/data0/jillian/h568/density1000/h568.cosmo75.4096gsHsbBH.BHmergers' 
data= np.loadtxt(file)

ratio = data[:,4]
timeMer = abs(data[:,6])

mUnit = 5.15549e16
lUnit = 74327.3

n= 6.67e-11*(1/2.938e57)*(1.989e30)*(mUnit)*(1/(lUnit**3)) 
print(n)
tMod= sqrt(1/n)
print(tMod)
timeMer=timeMer*tMod
timeMer=timeMer/3.154e16

plt.hist(ratio, bins=10)
plt.xlabel("Mass Ratio")
plt.ylabel("# of Black Holes")
plt.show()

    
    


