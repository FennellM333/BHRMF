import numpy as np
import matplotlib.pyplot as plt
import pynbody

# Load the simulation
file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000464"
s = pynbody.load(file)
s.physical_units()

# Load halo IDs
halos = np.loadtxt('haloIDI.txt', dtype=np.int32)
starHalos = list(halos)

# Load halo catalog
h = pynbody.halo.ahf.AHFCatalogue(s)

# Extract halo masses
hMass = []
for i in starHalos:
    try:
        mHalo = h[i].properties['mass']
        hMass.append(mHalo)
    except (ValueError, KeyError):
        continue

# Find black holes in the simulation
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)

# Find the halos that have black holes
def locBHhalos(BH):
    BHhalos = BH['amiga.grp']
    BHhalos = np.unique(BHhalos)
    return BHhalos

BHhalos = locBHhalos(BH)

# Extract masses of black hole halos
BHaloMass = []
for i in BHhalos:
    try:
        BHaloMass.append(h[i].properties['mass'])
    except (ValueError, KeyError):
        continue

# Flatten arrays
hMass = np.array(hMass).flatten()
BHMass = np.array(BHaloMass).flatten()

# Define bPoints and midpoints
numBins = 5
start = 6.5
end = 10
step = (end - start) / numBins
bPoints = np.arange(start, end + step, step)

# Calculate midpoints
midB = [(bPoints[i] + bPoints[i + 1]) / 2 for i in range(len(bPoints) - 1)]

# Create bin edges: first bin from bPoints[0] to midB[0], midB[i-1] to midB[i] for others, midB[-1] to bPoints[-1]
bin_edges = [bPoints[0]] + midB + [bPoints[-1]]

# Function to assign masses to bins based on bin edges
def assign_to_custom_bins(mass_array, bin_edges):
    bins = []
    for i in range(len(bin_edges) - 1):
        bins.append(mass_array[(mass_array >= bin_edges[i]) & (mass_array < bin_edges[i + 1])])
    return bins

# Assign hMass and BHMass to custom bins
hMassBin = assign_to_custom_bins(hMass, bin_edges)
BHMassBin = assign_to_custom_bins(BHMass, bin_edges)

# Verify results
print("hMassBin counts:", [len(bin) for bin in hMassBin])
print("BHMassBin counts:", [len(bin) for bin in BHMassBin])

# Calculate average mass per bin and BH fraction
avgMass = []
for i in range(numBins):
    combined_masses = np.concatenate((hMassBin[i], BHMassBin[i]))
    if len(combined_masses) > 0:
        avgMass.append(np.mean(combined_masses))
    else:
        avgMass.append(0)

avgLMass = np.log10(avgMass)
print("Average log mass per bin:", avgLMass)

numHalos = [len(hMassBin[i]) for i in range(numBins)]
numBH = [len(BHMassBin[i]) for i in range(numBins)]
print("Number of halos per bin:", numHalos)
print("Number of BHs per bin:", numBH)

bhFract = [numBH[i] / numHalos[i] if numHalos[i] > 0 else 0 for i in range(numBins)]
print("BH fractions per bin:", bhFract)

# Plotting the results
plt.plot(avgLMass, bhFract, marker='o')
plt.ylim(0, 1)
plt.xlabel('Mean Mass (log M☉)')
plt.ylabel('BH Fraction')
plt.title("BH Fraction Graph")
plt.show()

