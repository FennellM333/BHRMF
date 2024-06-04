
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('textTableN.txt') #load data

BHid = data[:,0] #converts colums of our text file into arrays
dCen = data[:,1]# ''
dCen = np.log10(dCen) 
timeBH = data[:,2]# '' 

uniqueBHid = np.unique(BHid)  #finds unique black hole ideas and sorts them

plt.figure(figsize=(10, 6)) #initializes the figure

for id in uniqueBHid: #loops the plotting function for each unique black hole
    aragorn = np.where(BHid == id) #makes sure the id being referenced in the loop is the id being plotted
    gimli = dCen[aragorn[0]] # makes sure the function only indexes 1 value
    legolas = timeBH[aragorn[0]] # '' 
    plt.plot(legolas, gimli, label=f'BH {id}') 

plt.xlabel("Time (Gyr)")
plt.ylabel("Log Distance from Galaxy Center (kpc)")
plt.title("Log Distance from Center Over Time for Different Black Holes")
plt.tight_layout()  # Adjust layout
plt.show()
