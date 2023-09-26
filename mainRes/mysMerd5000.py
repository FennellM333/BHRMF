import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

file =  '/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.BHmergers'
print(data)

ratio = data[:,4]
timeMer = data[:,6]

plt.hist(ratio, bins=10)
plt.xlabel("Mass Ratio")
plt.ylabel("# of Black Holes")
plt.show()


