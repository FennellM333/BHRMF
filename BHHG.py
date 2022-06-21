import pynbody
import numpy as np
import matplotlib.pylab as plt

file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
sl = pynbody.snapshot.tipsy.StarLog(file)

blackhole = np.where(sl['tform'] < 0.0)

tempBH = sl[blackhole[0]]['tempform']
rhoBH = sl[blackhole[0]]['rhoform']

x = np.log10(rhoBH)
y = np.log10(tempBH)

plt.hist2d(x,y,bins = 250, range = [[6,10],[1.4,3.5]])
plt.xlim([6,10])
plt.ylim([1.4,3.5])

plt.xlabel("Density")
plt.ylabel("Temperature")
plt.show()
