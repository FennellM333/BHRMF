import pynbody
import numpy as np
import matplotlib.pylab as plt



sl = pynbody.snapshot.tipsy.StarLog(file)

blackhole = np.where(sl['tform'] < 0.0)
sl.physical_units()

tBH = sl[blackhole[0]]['tform']

tBH = tBH*(-1)

plt.hist(tBH, bins =50, alpha=0.5, label='Black Holes')
plt.legend(loc='upper right')
plt.xlabel("Time (Gyr)")
plt.ylabel("# of Stellar Objects")

plt.show()