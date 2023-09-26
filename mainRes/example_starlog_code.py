"""
the goal of this code is to give an example of how to read a starlog file
"""

import pynbody
import numpy as np
import matplotlib.pyplot as plt


file = '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.starlog'
# read in the file
sl = pynbody.snapshot.tipsy.StarLog(file)


print("What is in this file?")
print(sl.keys())

# this is information for all the stars that formed in this simulation since the beginning of the universe
# cool, let's plot things


plt.hist(sl['tform'],bins=100)
plt.xlabel("formation time (units?)")
plt.ylabel("Number of stars")
plt.show()


# what the heck?
# ah, remember that black holes are identified by a negative formation time

star = np.where(sl['tform'] > 0.0)
blackhole = np.where(sl['tform'] < 0.0)
print(len(star[0])," stars")
print(len(blackhole[0])," black holes")


# your assignment: can you plot the information of formation times for just the stars?
# what about just the black holes?  (but switch the times to positive)

# your second assignment is to create a 2-d histogram of the quantities Temperature vs Density

