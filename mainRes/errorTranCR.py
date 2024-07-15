import numpy as np
import matplotlib.pyplot as plt
import pynbody

# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000464"
s = pynbody.load(file)
s.physical_units()

h = s.halos()
print(f"Total number of halos: {len(h)}")

#removing no-stars
w = h.stars == 0 
h = h[w]
print(f"Number of halos with stars {len(h)}")
"""
# Function to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return B

# Function to find the halos that have black holes
def findBHhalos(halos):
    BHhalos = []
    for i in range(1, len(halos) + 1):
        try:
            halo = halos[i] 
            BH = findBH(halo)
            if len(BH) > 0:
                BHhalos.append(halo)
        except (ValueError, KeyError):
            continue
    return BHhalos

print("Defined BHs")
BH = findBH(s)
BHid = BH['iord']

print("Defined halos with BHs")
BHhalos = findBHhalos(h)
print(f"Number of halos with BHs: {len(BHhalos)}")


hMass = []
for i in range(1, len(h) + 1):
    try:
        hMass.append(h[i]['mass'])
        print(f"Halo {i} mass added")
    except (ValueError, KeyError):
        # Skip this index if it does not exist
        continue
    
BHMass = []
for i in range(22):
    try:
        BHMass.append(BH[i]['mass'])
        print(f"Halo {i} mass added")
    except (ValueError, KeyError):
        # Skip this index if it does not exist
        continue

print("hMass", hMass)
print("BHMass", BHMass)

#there does not seem to be a way to make this a variable number but I will keep trying
numBin = 7

#this uses bin edges to put both array's masses into the bins
bothMass = npconcatenate(hMass, BHMass)
bEdge = np.linspace (bothMass.min(), bothMass.max(), numBins + 1)
#function to actually make the bins
def  marrayE(hMass, bEdge):
    mBins = [hMass[(hMass >= bEdge[i]) & (hMass <bEdge[i+1])]for i in range(len(bEdge)-1)]
    return mBins

def  marrayE(BHMass, bEdge):
    mBins = [BHMass[(hMass >= bEdge[i]) & (BHMass <bEdge[i+1])]for i in range(len(bEdge)-1)]
    return mBins

hMassBin = murrayE(np.array(hMass), bEdge)
BHMassBin = murrayE(np.array(BHMass), bEdge)

avgMass = [(np.mean(np.concatenate((hMass_bins[i], BHMass_bins[i]))) if len(hMass_bins[i]) + len(BHMass_bins[i]) > 0 else 0) for i in range(num_bins)]

numHalos = [len(hMassBin[i]) for i in range(numBin)]
numBH = [len(BHMassBin[i]) for i in range(numBin)]
bhFract = [numBH[i] / numHalos[i] if numHalos[i] > 0 else 0 for i in range(numBin)]

print("halos without black holes in each group", numHalos)
print("halos with black holes in each group",numBH)
print("BH fractions", bhFract)

plt.figure(figsize(10,6))
plt.errorbar(avgMass , bhFract)
plt.yscale('log')
plt.xlabel('Mean Mass (M☉)')
plt.ylabel('BH Fraction')
plt.title("BH Fraction Graph")
plt.show()
"""