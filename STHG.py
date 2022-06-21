import pynbody
import numpy as np
import matplotlib.pylab as plt

file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

star = np.where(sl['tform'] > 0.0)

tempST = sl[star[0]]['tempform']
rhoST = sl[star[0]]['rhoform']

x = np.log10(rhoST)
y = np.log10(tempST)

plt.hist2d(x,y,bins = 250, range = [[6,10],[1.4,3.5]])
plt.xlabel("Density")
plt.ylabel("Temperature")
plt.show()