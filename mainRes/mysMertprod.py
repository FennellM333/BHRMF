from cmath import sqrt
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

file =  '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.BHmergers'
data= np.loadtxt(file)
print(data)

ratio = data[:,4]
timeMer = abs(data[:,6])

mUnit = 5.15549e16
lUnit = 74327.3

n= 6.67e-11*(1/2.938e58)*(1.989e30)*(mUnit)*(1/(lUnit**3)) 
print(n)
tMod= sqrt(1/n)
print(tMod)
timeMer=timeMer*tMod
timeMer=timeMer/3.154e16

new_list = range(4)
print('new_list')

plt.yticks(new_list)
plt.hist(timeMer, bins=5)
plt.xlabel("Time of Merger (Gyr.)")
plt.ylabel("# of Black Holes")
plt.show()
plt.savefig(mysMertprod)


