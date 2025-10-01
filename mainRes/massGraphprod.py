import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

filename =  '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000464'

s = pynbody.load(filename)
h = s.halos()
s.physical_units()
y= []
x = []

def  locBH(s):      
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter] 
    return BH
BH = locBH(s)
BHid = BH['iord']

def  locBHhalos(s, BH):
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = locBHhalos(s,BH)

for i in range(len(BH)): 
    if BHhalos[i] == 0:
        print("Halo = 0, skip.")
        continue
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
    bhMass = BH['mass'][i]
    starMass= h[BHhalos[i]].s['mass'].sum() -bhMass
    lstarMass = np.log10(starMass)
    lbhMass = np.log10(bhMass)
    y.append(lstarMass)
    x.append(lbhMass)

plt.plot(y,x,'bo')
plt.title("Density Threshold 5000")
plt.ylabel("Black Hole Mass (Msol)")
plt.xlabel("Star Mass (Msol)")
plt.show()
