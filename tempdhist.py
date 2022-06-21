import pynbody
import numpy as np
import matplotlib.pylab as plt

file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

blackhole = np.where(sl['tform'] < 0.0)
star = np.where(sl['tform'] > 0.0)

tempST = sl[star[0]]['tempform']
tempBH = sl[blackhole[0]]['tempform']

sT = np.log10(tempST)
bH = np.log10(tempBH)


plt.hist(sT, bins = 1000, alpha=0.5, density = 1 ,  label='Stars')
plt.hist(bH, bins =1000, alpha=0.5, density = 1, label='Black Holes')
plt.legend(loc='upper right')
plt.xlabel("Temperature")
plt.ylabel("# of Stellar Objects")
plt.show()