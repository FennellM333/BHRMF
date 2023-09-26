import pynbody
import numpy as np
import matplotlib.pylab as plt

file = '/mnt/data0/jillian/h568/density10/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

blackhole = np.where(sl['tform'] < 0.0)
star = np.where(sl['tform'] > 0.0)

rhoST = sl[star[0]]['rhoform']
rhoBH = sl[blackhole[0]]['rhoform']

sT = np.log10(rhoST)
bH = np.log10(rhoBH)


#plt.hist(sT, bins = 1000, alpha=0.5,  label='Stars')
plt.hist(bH, bins =100, alpha=0.5, label='Black Holes')
plt.legend(loc='upper right')
plt.xlabel("Density")
plt.ylabel("# of Stellar Objects")
plt.show()