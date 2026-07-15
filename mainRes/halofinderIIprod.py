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
BHhalos = BH['amiga.grp']
print("BH count:", len(BH))

# Use particle index as ID since iord isn't loadable for this snapshot
BHid = np.arange(len(BH))

dCen = []
validBH   = []
validHalo = []
validDist = []

for i in range(len(BH)):
    print(i)
    if BHhalos[i] == 0:
        print(f"  BH {i}: halo=0, skipping.")
        continue
    try:
        pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
        pos = BH['pos'][i]
        d = float(np.sqrt((pos**2).sum()))
        dCen.append(d)
        validBH.append(BHid[i])
        validHalo.append(BHhalos[i])
        validDist.append(d)
    except Exception as e:
        print(f"  BH {i} halo {BHhalos[i]} failed: {e}")
        continue

print(f"\n{len(dCen)} BHs with valid halo centers.")

with open('foundprod.txt', 'w') as f:
    f.write("       |BH ID|          |Galaxy ID|   |Distance from Center|\n")
    for a, b, c in zip(validBH, validHalo, validDist):
        f.write('{0:15}{1:15}         {2:.5}\n'.format(a, b, c))

plt.figure()
plt.hist(dCen, bins=50, range=(0, 10))
plt.xlabel("Distance (kpc)")
plt.ylabel("# of Black Holes")
plt.tight_layout()
plt.savefig("foundprod.png")
plt.show()
"""
import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

filename =  '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000320'

# iord? that should give each black hole a unique id to match eventually with their respective halo
s = pynbody.load(filename)
h = s.halos()
s.physical_units()

#filters our stars into black holes
def  locBH(s):      
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter] 
    return BH
BH = locBH(s)
BHid = BH['iord']

#this should filter those black holes further to only those with halos
def  locBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = locBHhalos(s)

dCen = []

for i in range(len(BH)):#starts the loop that will check how far each black hole is from their respective halos
    print(i) 
    if BHhalos[i] == 0: #skips over all the black holes with no halos 
        continue
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb') #actually centers the snapshot on each halo
    x=BH['pos'][[i],0]
    y=BH['pos'][[i],1]
    z=BH['pos'][[i],2]
    #aquires the x y and z coordinates of each black hole relative to its respective center
    dCen.append(((x**2+y**2+z**2)**0.5)[0]) #creates an array of the distances for each black hole

#ok actually this is a loop I lied but this is what I used to format the array into the text file
with open('foundprod.txt' , 'w') as f:
    f.write("       |BH ID|          |Galaxy ID|   |Distance from Center|   \n") 
    for a,b,c in zip(BHid,BHhalos,dCen):
        f.write('{0:15}{1:15}         {2:.5}\n'.format(a,b,c))  

print(len(BH))

plt.hist(dCen, bins=50, range = (0,10))
plt.xlabel("Distance (kpc)")
plt.ylabel("# of Black Holes")
plt.show()
"""