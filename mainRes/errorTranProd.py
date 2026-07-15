import numpy as np
import matplotlib.pyplot as plt
import pynbody
import scipy.stats

# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000320"
s = pynbody.load(file)
s.physical_units()

# Force-load iord if available
try:
    s.load_copy('iord')
except Exception as e:
    print(f"iord load attempt: {e}")

halos = np.loadtxt('haloIDI.txt', dtype=np.int32)
starHalos = list(halos)

h = pynbody.halo.ahf.AHFCatalogue(s, write_fpos=False)

print("Number of starHalos:", len(starHalos))

# --- Probe halo properties to find the mass key ---
mass_key = None
for test_id in starHalos[:10]:
    try:
        props = dict(h[test_id].properties)
        print(f"Halo {test_id} property keys: {list(props.keys())}")
        for candidate in ['mass', 'Mvir', 'M_vir', 'Mhalo', 'mvir', 'm_vir']:
            if candidate in props:
                mass_key = candidate
                print(f"Found mass key: '{mass_key}' = {props[mass_key]}")
                break
        if mass_key:
            break
    except Exception as e:
        print(f"  Probe halo {test_id} failed: {e}")
        continue

if mass_key is None:
    raise RuntimeError("Could not find a mass key in halo properties. Check the probe output above.")

print(f"\nUsing mass key: '{mass_key}'")

# Loop through each halo and find its mass
hMass = []
for i in starHalos:
    try:
        mHalo = h[i].properties[mass_key]
        hMass.append(mHalo)
    except (ValueError, KeyError):
        continue

print("Number of hMass:", len(hMass))

# Defines black holes (star particles with negative tform)
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.star[BHfilter]
    return BH

BH = findBH(s)
print("BH count:", len(BH))

# Function to find the halos that contain black holes
def locBHhalos(BH):
    BHhalos = BH['amiga.grp']
    BHhalos = np.unique(BHhalos)
    return BHhalos

BHhalos = locBHhalos(BH)
print("Defined BH halos:", BHhalos)

# Finding the mass of halos that contain black holes
BHaloMass = []
for i in range(len(BHhalos)):
    try:
        BHaloMass.append(h[BHhalos[i]].properties[mass_key])
    except (ValueError, KeyError):
        continue

print("Number of BHaloMass:", len(BHaloMass))

if len(hMass) == 0 or len(BHaloMass) == 0:
    print("ERROR: hMass or BHaloMass is empty — check probe output above.")
else:
    hMass   = np.log10(np.array(hMass))
    BHhMass = np.log10(np.array(BHaloMass))

    Mmin = hMass.min()
    Mmax = hMass.max()
    print(f"Mmin={Mmin}, Mmax={Mmax}")

    numBins = 5
    binsize = (Mmax - Mmin) / numBins
    print(f"binsize={binsize}")

    def binomial_errors(confidence, ntrue, ntot):
        if ntot <= 0:
            return 0, 0
        alpha = 1 - confidence
        lo = 0.0 if ntrue <= 0 else scipy.stats.beta.ppf(alpha / 2, ntrue, ntot - ntrue + 1)
        hi = 1.0 if ntrue == ntot else scipy.stats.beta.ppf(1 - alpha / 2, ntrue + 1, ntot - ntrue)
        return lo, hi

    counts  = []
    Bcounts = []
    BHfract = []

    for i in range(numBins):
        lo_edge = Mmin + binsize * i
        hi_edge = Mmin + binsize * (i + 1)
        count  = np.count_nonzero((hMass  >= lo_edge) & (hMass  <= hi_edge))
        Bcount = np.count_nonzero((BHhMass >= lo_edge) & (BHhMass <= hi_edge))
        counts.append(count)
        Bcounts.append(Bcount)
        BHfract.append(Bcount / count if count > 0 else 0.0)

    nub   = np.arange(numBins)
    xVals = Mmin + binsize * nub + binsize / 2

    uppers = []
    lowers = []
    for i in range(len(counts)):
        ntrue = Bcounts[i]
        ntot  = counts[i]
        if ntot > 0:
            lo, hi = binomial_errors(0.95, ntrue, ntot)
            frac = ntrue / ntot
            lowers.append(max(0, frac - lo))
            uppers.append(max(0, hi - frac))
        else:
            uppers.append(0)
            lowers.append(0)

    Berror = np.array([lowers, uppers])

    print("x values:", xVals)
    print("y values:", BHfract)
    print("error array:", Berror)

    plt.rc('xtick', labelsize=15)
    plt.rc('ytick', labelsize=15)
    plt.rc('font', weight='bold', size=13)

    plt.figure()
    plt.errorbar(xVals, BHfract, yerr=Berror, fmt='o', color='black',
                 ecolor='black', capsize=6, linewidth=2, markersize=8)
    plt.xlabel('Log Halo Mass (M☉)')
    plt.ylabel('BH Occupation Fraction')
    plt.title("BH Occupation Fraction")
    plt.tight_layout()
    plt.savefig("BhgraphProd.png")
    plt.show()
"""
import numpy as np
import matplotlib.pyplot as plt
import pynbody
import scipy.stats 

# Define directories and files
file = "/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.000320"
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

counts=[]
Bcounts=[]
Mavg=[]
BHfract=[]
cBin=[]

for i in range(numBins):
    count= np.count_nonzero((hMass>=(Mmin+(binsize*i)))&(hMass<=(Mmin+(binsize*(i+1)))))
    Mavgs= np.mean((hMass>=(Mmin+(binsize*i)))&(hMass<=(Mmin+(binsize*(i+1)))))
    Bcount= np.count_nonzero((BHhMass>=(Mmin+(binsize*i)))&(BHhMass<=(Mmin+(binsize*(i+1)))))
    print("Bcount-", Bcount)
    Bcounts.append(Bcount)
    print("count-", count)
    counts.append(count)
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
#print("xVals", xVals)


#Error bars, still unclear on exactly what this is doing or how to impliment it.
def binomial_errors(confidence,  ntrue, ntot):
    if ntot <= 0: 
        return 0, 0 

    alpha = 1 - confidence
    if ntrue <= 0:
        lo = 0.0
    else:
        lo = scipy.stats.beta.ppf(alpha / 2, ntrue,  ntot -ntrue +1)
    if ntrue == ntot:
        hi = 1.0
    else:
        hi= scipy.stats.beta.ppf(1-alpha / 2, ntrue +1,  ntot -ntrue)
    #lo = scipy.stats.beta.ppf(alpha / 2, ntrue, ntot - ntrue + 1) 
    #hi = scipy.stats.beta.ppf(1 - alpha / 2, ntrue + 1, ntot - ntrue)
    
    return lo, hi

uppers= []
lowers= []

for i in range (len(counts)):
    ntrue = Bcounts[i]
    ntot= counts[i]
    if ntot > 0:
        lo, hi = binomial_errors(.95,ntrue,ntot) 
        frac = ntrue/ntot 
        print('lo-', lo)
        print('hi-',hi)
        #upper_offset= hi - current_frac
        #lower_offset = current_frac -lo 
        lowers.append(max(0, frac-lo))
        uppers.append(max(0, hi - frac))
    else:
        uppers.append(0)
        lowers.append(0)
boths=np.column_stack((uppers,lowers))
# Verify results
#print("hMassBin counts:", [len(bin) for bin in hMassBin])
#print("BHMassBin counts:", [len(bin) for bin in BHMassBin]
#avgMass = [(np.mean(np.concatenate((hMassBin[i], BHMassBin[i]))) if len(hMassBin[i]) + len(BHMassBin[i]) > 0 else 0) for i in range(numBins)]
#avgLMass = np.log10(avgMass)
#print("Average log mass per bin:", avgLMass)
Berror= np.array([lowers,uppers])
print("x values - ", xVals )
print("y values - ", BHfract)
print("error array-", Berror)

plt.rc('xtick', labelsize = 15)
plt.rc('ytick', labelsize = 15)
font = {'weight' : 'bold',
        'size'   : 13}
plt.rc('font', **font)
plt.plot(xVals, BHfract, marker='o')
plt.errorbar(xVals, BHfract,yerr= Berror, fmt= 'o', color = 'black', ecolor= 'black', capsize=6, linewidth=2, markersize=8)
plt.xlabel('Log Halo Mass (M☉)')
plt.ylabel('BH Occupation Fraction')
plt.title("BH Occupation Fraction")
plt.savefig("Bhgraph.png")
plt.show()
"""