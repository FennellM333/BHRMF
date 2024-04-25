import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('timeTable.txt')

BHid = data[:,0]
dCen = data[:,1]
timeBH = data[:,2]

uniqueBHid = np.unique(BHid)

plt.figure(figsize=(10, 6))

for id in uniqueBHid:
    aragorn = np.where(BHid == id)
    gimli = dCen[aragorn[0]]
    legolas = timeBH[aragorn[0]]
    plt.plot(legolas, gimli, label=f'BH {id}')

plt.xlabel("Time (Gyr)")
plt.ylabel("Distance from Galaxy Center (kpc)")
plt.title("Distance from Center Over Time for Different Black Holes")
plt.legend(loc='upper right', fontsize=8)  # Show legend without labels
plt.grid(True)  # Add grid for better readability
plt.tight_layout()  # Adjust layout
plt.show()

plt.show()
