import numpy as np
import matplotlib.pyplot as plt
import pynbody 

# Define directories and files

file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000464"
s = pynbody.load(file)
print(s) 
s.physical_units

h = s.halos()
print(len(h))

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
print("defined BHs")
BH= findBH(s)
BHid = BH['iord']
#function to find the halos that have blackholes
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
print("define halos")
#using the function the halos
BHhalos = findBHhalos(s)
print(len(BHhalos))

hMass = []
for i in range(1, len(h) + 1):
    try:
        hMass.append(h[i]['mass'])
        print(i)
    except ValueError:
        # Skip this index if it does not exist
        continue
    
#binning masses randomly for now
print("all mass values:", hMass)
m1, m2, m3, m4 = map(list, zip(*zip(*[iter(hMass)]*4)))

#uisng this for the BH fraction of each bin
num1halo= len(m1)
num2halo= len(m2)
num3halo= len(m3)
num4halo= len(m4)

print("halos in group 1", num1halo)
print("halos in group 2", num2halo)
print("halos in group 3", num3halo)
print("halos in group 4", num4halo)

#black hole count for ratio
m1BH = findBHhalos(m1)
m2BH= findBHhalos(m2)
m3BH= findBHhalos(m3)
m4BH= findBHhalos(m4)

num1BH= len(m1BH)
num2BH= len(m2BH)
num3BH= len(m3BH)
num4BH= len(m4BH)

print("black holes in group 1", num1BH)
print("black holes in group 2", num2BH)
print("black holes in group 3", num3BH)
print("black holes in group 4", num4BH)

#BH fraction
fract1 = num1BH/num1halo
fract2 = num2BH/num2halo
fract3 = num3BH/num3halo
fract4 = num4BH/num4halo


m1p = mean(m1)
m2p = mean(m2)
m3p = mean(m3)
m4p = mean(m4)

fractG= [fract1,fract2,fract3,fract4]
mG= [m1p,m2p,m3p,m4p]

print("fractG", fractG)
print("mG", mG)

plt.figure(figsize=(10, 6))
plt.errorbar(fractG,mG)
plt.yscale('log')
plt.xscale('linear')
plt.ylim(1e-5, 2)
plt.xlim(6, 12.5)
plt.xlabel('log Halo Mass (M☉)')
plt.ylabel('BH Fraction')
plt.title('Occupation Fraction')
plt.grid(True)
plt.savefig('occupationfraction.png')
plt.show()
