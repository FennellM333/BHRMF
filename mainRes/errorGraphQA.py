import numpy as np
import matplotlib.pyplot as plt
import pynbody
import scipy.stats 

xVals=  [ 6.17213211,  7.13561429,  8.09909647,  9.06257865, 10.02606083]
yVals= [0.0, 0.017857142857142856, 0.0392156862745098, 0.045112781954887216, 0.4090909090909091]
uppers= [0.30849711, 0.07766876, 0.0953708,  0.05049198, 0.22736213]
lowers= [0,  0.01740514, 0.03443069, 0.02837971, 0.20199779]
errArr= np.array([uppers,lowers])
plt.rc('xtick', labelsize = 15)
plt.rc('ytick', labelsize = 15)
font = {'weight' : 'bold',
        'size'   : 13}
plt.rc('font', **font)
plt.plot(xVals, yVals, marker='o')
plt.errorbar(xVals, yVals,yerr= errArr, fmt= 'o', color = 'black', ecolor= 'black', capsize=6, linewidth=2, markersize=8)
plt.xlabel('Log Halo Mass (M☉)')
plt.ylabel('BH Occupation Fraction')
plt.title("BH Occupation Fraction")
plt.savefig("Bhgraph.png")
plt.show()