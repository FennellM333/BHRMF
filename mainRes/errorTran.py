import numpy as np
import matplotlib.pyplot as plt
import pynbody


# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun2023/h568.cosmo75.4096gsHsbBH.000464"
s = pynbody.load(file)
s.physical_units()
halos = np.loadtxt('haloIDI.txt', dtype=np.int32)
starHalos = list(halos)

# New halo array
h = pynbody.halo.ahf.AHFCatalogue(s)

print("Number of starHalos:", len(starHalos))

# Loop through each halo and find its mass
hMass = []
for i in starHalos:
    try:
        mHalo = h[i].properties['mass']
        hMass.append(mHalo)
    except (ValueError, KeyError):
        continue

print("Number of hMass:", len(hMass))

# Defines black holes in the simulation
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)
BHid = BH['iord']

# Function to find the halos that have black holes
def locBHhalos(BH):
    BHhalos = BH['amiga.grp']
    BHhalos = np.unique(BHhalos)
    return BHhalos

BHhalos = locBHhalos(BH)
print("Defined BH halos:", BHhalos)

# Finding the mass of black holes
BHaloMass = []
for i in range(len(BHhalos)):
    try:
        BHaloMass.append(h[BHhalos[i]].properties['mass'])
    except (ValueError, KeyError):
        continue

print("Number of BHaloMass:", len(BHaloMass))

# Flatten the arrays
hMass = np.array(hMass)#.flatten()
BHhMass = np.array(BHaloMass)#.flatten()

hMass =np.log10(hMass)
BHhMass =np.log10(BHhMass)

Mmin = min(hMass)
Mmax = max(hMass)
print("Mmin=", Mmin)
print("Mmax=", Mmax)


# Combine the arrays
# bothMass = np.concatenate((hMass, BHMass))

# Number of bins
numBins = 5

binsize = (Mmax-Mmin)/numBins 
print("binsize= ", binsize)

# Sort the combined array
#sorted_masses = np.sort(bothMass)

# Split the sorted array into bins with an even distribution of points
#bins = np.array_split(sorted_masses, numBins)

# Function to determine the bin edges from sorted masses
#bin_edges = np.linspace(min(BHMass), max(BHMass), numBins +1)
#bin_edges.append(bins[-1][-1])  # Add the last edge

#print("Bin edges:", bin_edges)

# Create a function to assign original masses to bins
#def assign_to_bins(mass_array, bin_edges):
    #bin_indices = np.digitize(mass_array, bin_edges) - 1
    #bins = [mass_array[bin_indices == i] for i in range(len(bin_edges) - 1)]
    #return bins

# Assign hMass and BHMass to bins
#hMassBin = assign_to_bins(hMass, bin_edges)
#BHMassBin = assign_to_bins(BHMass, bin_edges)

#counts=[]
#Bcounts=[]
Mavg=[]
BHfract=[]
cBin=[]

for i in range(numBins):
    count= np.count_nonzero((hMass>=(Mmin+(binsize*i)))&(hMass<=(Mmin+(binsize*(i+1)))))
    Mavgs= np.mean((hMass>=(Mmin+(binsize*i)))&(hMass<=(Mmin+(binsize*(i+1)))))
    Bcount= np.count_nonzero((BHhMass>=(Mmin+(binsize*i)))&(BHhMass<=(Mmin+(binsize*(i+1)))))
    print("Bcount-", Bcount)
    #Bcounts.append(Bcount)
    print("count-", count)
    #counts.append(count)
    print("average-",Mavg)
    Mavg.append(Mavgs)
    print("Average Bin Mass-", Mavg)
    BlHf= Bcount/count
    BHfract.append(BlHf)
    print("BHfract-", BHfract)
    cBin.append(i)


nub = np.arange(numBins)
print("nub-", nub)
xVals = Mmin +binsize*nub + binsize/2
print("xVals", xVals)







# Verify results
#print("hMassBin counts:", [len(bin) for bin in hMassBin])
#print("BHMassBin counts:", [len(bin) for bin in BHMassBin])

#avgMass = [(np.mean(np.concatenate((hMassBin[i], BHMassBin[i]))) if len(hMassBin[i]) + len(BHMassBin[i]) > 0 else 0) for i in range(numBins)]
#avgLMass = np.log10(avgMass)
#print("Average log mass per bin:", avgLMass)


plt.rc('xtick', labelsize = 9)
plt.rc('ytick', labelsize = 9)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 13}
plt.rc('font', **font)
plt.plot(xVals, BHfract, marker='o')
#plt.yscale('log')
plt.xlabel('Log Halo Mass (M☉)')
plt.ylabel('BH Occupation Fraction')
plt.title("BH Occupation Fraction")
plt.show()
