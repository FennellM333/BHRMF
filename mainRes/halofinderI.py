import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 
import pylab 

file =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

s = pynbody.load(file)

#initializes the command to find black holes
BHfilter = pynbody.filt.LowPass('tform',0.0)
BH = s.stars[BHfilter]

BHhalos = BH['amiga.grp']

#
h = s.halos()  
h1 = h[1]
s.physical_units()  
BHfilter = pynbody.filt.LowPass('tform',0.0) 

pynbody.analysis.halo.center(h[1], mode='hyb')

pynbody.plot.image(h1.g, width=100, cmap='Greys')

plt.show()