import matplotlib.pyplot as plt
import numpy as np

data = '/home/fennell/BHRMF/mainRes/foundTLT.txt'
data = np.genfromtxt(data, dtype= str)

plt.plot(data)

plt.show()