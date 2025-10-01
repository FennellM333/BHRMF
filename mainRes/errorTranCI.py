import numpy as np
import matplotlib.pyplot as plt
import pynbody

# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000464"
s = pynbody.load(file)
s.physical_units()
halos = np.loadtxt('haloIDI.txt', dtype=np.int32)
starHalos = list(halos)

# New halo array
h = pynbody.halo.ahf.AHFCatalogue(s)

print(len(starHalos))

# Loop through each halo and find its mass
hMass = []
for halo_id in starHalos:
    try:
        mHalo = h[halo_id].properties['mass']
        print(mHalo)
        hMass.append(mHalo)
        print(f"Halo {halo_id} mass added")
    except (ValueError, KeyError):
        # Skip this index if it does not exist
        continue

# Defines black holes in the simulation
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

print("Defined BHs")
BH = findBH(s)
BHid = BH['iord']

# Function to find the halos that have black holes
def locBHhalos(BH):
    BHhalos = BH['amiga.grp']
    return BHhalos

BHhalos = locBHhalos(BH)
print(f"Defined halos with BHs {BHhalos}")

# Finding the mass of black holes
BHMass = []
for i in range(len(BH)):
    try:
        BHMass.append(BH[i]['mass'])
        print(f"Black hole {i} mass added")
    except (ValueError, KeyError):
        # Skip this index if it does not exist
        continue

print("BHMass", BHMass)

# Binning the masses
numBins = 7
bothMass = np.concatenate((hMass, BHMass))
bEdge = np.linspace(bothMass.min(), bothMass.max(), numBins + 1)

# Function to bin masses
def bin_masses(mass_array, bEdge):
    mBins = [mass_array[(mass_array >= bEdge[i]) & (mass_array < bEdge[i+1])] for i in range(len(bEdge) - 1)]
    return mBins

hMassBin = bin_masses(np.array(hMass), bEdge)
BHMassBin = bin_masses(np.array(BHMass), bEdge)

avgMass = [(np.mean(np.concatenate((hMassBin[i], BHMassBin[i]))) if len(hMassBin[i]) + len(BHMassBin[i]) > 0 else 0) for i in range(numBins)]

numHalos = [len(hMassBin[i]) for i in range(numBins)]
numBH = [len(BHMassBin[i]) for i in range(numBins)]
bhFract = [numBH[i] / numHalos[i] if numHalos[i] > 0 else 0 for i in range(numBins)]

print("Halos without black holes in each group", numHalos)
print("Halos with black holes in each group", numBH)
print("BH fractions", bhFract)

plt.figure(figsize=(10, 6))
plt.plot(avgMass, bhFract, marker='o')
plt.yscale('log')
plt.xlabel('Mean Mass (M☉)')
plt.ylabel('BH Fraction')
plt.title("BH Fraction Graph")
plt.show()
