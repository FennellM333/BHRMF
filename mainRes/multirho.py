import pynbody
import numpy as np
import matplotlib.pylab as plt

filenamelist = ''
sl = pynbody.snapshot.tipsy.StarLog(filenamelist)

blackhole = np.where(sl['tform'] < 0.0)
star = np.where(sl['tform'] > 0.0)

rhoST = sl[star[0]]['rhoform'] .in_units('m_p cm**-3')
rhoBH = sl[blackhole[0]]['rhoform'].in_units('m_p cm**-3')
