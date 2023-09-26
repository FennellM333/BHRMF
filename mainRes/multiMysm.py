from codecs import namereplace_errors
from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

filenamelist =  ['/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.BHmergers','/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.BHmergers',  '/mnt/data0/jillian/h568/density1000/h568.cosmo75.4096gsHsbBH.BHmergers' ,  '/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.BHmergers']
nfilenames = len(filenamelist)
dThresh = ["10 amu/cc", "100 amu/cc", "1000 amu/cc", "5000 amu/cc"]

mUnit = 5.15549e16
lUnit = 74327.3
vunit=1726.9381

for i in range(nfilenames):
    data= np.loadtxt(filenamelist[i])
    print(data)

    ratio = data[:,4]
    timeMer =abs(data[:,6])

  
    n= 6.67e-11*(1/2.938e58)*(1.989e30)*(mUnit)*(1/(lUnit**3)) 
    print(n)
    tMod= sqrt(1/n)
    print('tMod =' , tMod)
    timeMer=timeMer*tMod
    timeMer=timeMer/3.154e16

    plt.subplot()
    plt.hist(timeMer, bins=10, label= dThresh[i])
    plt.legend(loc = 'upper right')
    plt.xlabel("Time of Merger (Gyr.)")
    plt.ylabel("# of Mergers") 

plt.tight_layout
plt.show()
