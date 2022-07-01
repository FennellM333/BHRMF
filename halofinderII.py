import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 
import pylab 

filenamelist =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

# iord? that should give each black hole a unique id to match eventually with their respective halo

s = pynbody.load(filenamelist)

s.loadable_keys()
h = halos()

#filters our stars into black holes

BHfilter = pynbody.filt.LowPass('tform',0.0)
BH = s.stars[BHfilter] 

#this should filter those black holes further to only those with halos

BHhalos = BH['amiga.grp']

print(BHhalos)
      
#for center distance, find out what halos as in h1, h2, h3, etc... have the blackholes in them,
#then make the center of the snapshot the center of each galaxy, then calculate the distance from the center


#Idea for distance from center
#np.min(h.BHhalo['hyb'])