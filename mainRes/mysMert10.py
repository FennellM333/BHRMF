from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 
#dMsolUnit       = 5.15549e+16
#dKpcUnit        = 74327.3
file =  '/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.BHmergers'    
data= np.loadtxt(file)
print(data)

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

plt.hist(timeMer, bins=10)
plt.xlabel("Time of Merger(Gyr.)")
plt.ylabel("# of Black Holes")
plt.show()
