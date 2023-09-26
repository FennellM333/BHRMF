import pynbody
import numpy as np
import matplotlib.pylab as plt

filenamelist = ['/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.starlog', '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog','/mnt/data0/jillian/h568/density1000/h568.cosmo75.4096gsHsbBH.starlog','/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.starlog'] 
nfilenames = len(filenamelist)

for i in range(nfilenames):
   sl = pynbody.snapshot.tipsy.StarLog(filenamelist[i])

   blackhole = np.where(sl['tform'] < 0.0)

   rhoBH = sl[blackhole[0]]['rhoform'].in_units('m_p cm**-3')
   bHr = np.log10(rhoBH)
   plt.subplot(4,2,((2*i)+1))
   plt.hist(bHr, bins =50, range = (1,4.5))
   plt.xlabel("Log Density")
   
   tempBH = sl[blackhole[0]]['tempform']
   bHt= np.log10(tempBH)
   plt.subplot(4,2,((2*i)+2))
   plt.hist(bHt, bins =50, range =(2,3.5))
   plt.xlabel("Log Temperature")
    
plt.tight_layout()

plt.show()