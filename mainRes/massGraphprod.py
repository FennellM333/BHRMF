import pynbody
import numpy as np
import matplotlib.pyplot as plt

filename = '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000320'

s = pynbody.load(filename)
s.physical_units()
h = pynbody.halo.ahf.AHFCatalogue(s, write_fpos=False)

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    return s.star[BHfilter]

BH = findBH(s)
print("BH count:", len(BH))

# Get halo membership for each BH directly from amiga.grp
BHhalos = BH['amiga.grp']

x = []  # log BH mass
y = []  # log stellar mass

for i in range(len(BH)):
    halo_id = BHhalos[i]
    if halo_id == 0:
        print(f"BH {i}: halo=0, skipping.")
        continue
    try:
        pynbody.analysis.halo.center(h[halo_id], mode='hyb')
        bhMass   = BH['mass'][i]
        starMass = h[halo_id].s['mass'].sum() - bhMass
        if starMass <= 0:
            print(f"BH {i}: non-positive stellar mass, skipping.")
            continue
        x.append(np.log10(float(bhMass)))
        y.append(np.log10(float(starMass)))
    except Exception as e:
        print(f"BH {i} halo {halo_id} failed: {e}")
        continue

print(f"Plotted {len(x)} BH-halo pairs.")

plt.figure()
plt.plot(x, y, 'bo')
plt.title("Density Threshold 5000")
plt.xlabel("Log Black Hole Mass (M☉)")
plt.ylabel("Log Stellar Mass (M☉)")
plt.tight_layout()
plt.savefig("massGraph.png")
plt.show()
"""
import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

filename =  '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000320'

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
"""