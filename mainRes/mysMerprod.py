import numpy as np
import matplotlib.pyplot as plt

file = '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.BHmergers'

data = np.loadtxt(file, ndmin=2)
print(data)

if data.size == 0:
    print("BHmergers file is empty — no mergers to plot.")
else:
    ratio   = data[:, 4]
    timeMer = data[:, 6]

    plt.figure()
    plt.hist(ratio, bins=7)
    plt.xlabel("Mass Ratio")
    plt.ylabel("# of Black Holes")
    plt.tight_layout()
    plt.savefig("Ratio.png")
    print(f"Saved Ratio.png ({len(ratio)} mergers)")
    
"""
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pylab 

file =  '/mnt/data0/jillian/h568/productionrun/h568.cosmo75.4096gsHsbBH.BHmergers'
data= np.loadtxt(file)
print(data)

ratio = data[:,4]
timeMer = data[:,6]

plt.hist(ratio, bins=7)
plt.xlabel("Mass Ratio")
plt.ylabel("# of Black Holes")
plt.savefig("Ratio.png")
"""

