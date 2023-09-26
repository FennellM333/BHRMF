import pynbody
import numpy as np
import matplotlib.pylab as plt


filenamelist = ['/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.starlog', '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog','/mnt/data0/jillian/h568/density1000/h568.cosmo75.4096gsHsbBH.starlog','/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.starlog'] 
nfilenames = len(filenamelist)
dThresh = ["10 amu/cc", "100 amu/cc", "1000 amu/cc", "5000 amu/cc"]

for i in range(nfilenames):

   sl = pynbody.snapshot.tipsy.StarLog(filenamelist[i])


   sl.physical_units()

   tBH = sl[blackhole[0]]['tform']

   tBH = tBH*(-1)
   
   plt.hist(tBH, bins =50, alpha = 0.5, label = dThresh[i])
   plt.legend(loc='upper right')
   plt.xlabel("Time (Gyr)")
   plt.ylabel("# of Black Holes")

plt.tight_layout()
plt.show()