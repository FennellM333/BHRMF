import pynbody
import numpy as np
import matplotlib.pylab as plt

file = '/mnt/data0/jillian/h568/density5000/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

blackhole = np.where(sl['tform'] < 0.0)
#star = np.where(sl['tform'] > 0.0)
sl.physical_units()
#rhoST = sl[star[0]]['rhoform']
tBH = sl[blackhole[0]]['tform']

tBH = tBH*(-1)
#plt.hist(sT, bins = 1000, alpha=0.5,  label='Stars')
plt.hist(tBH, bins =50, alpha=0.5, label='Black Holes')
plt.legend(loc='upper right')
plt.xlabel("Time (Gyr)")
plt.ylabel("# of Stellar Objects")
plt.show()