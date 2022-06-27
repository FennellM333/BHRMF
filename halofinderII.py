import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 
import pylab 

filenamelist =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

s = pynbody.load(filenamelist)

#initializes the command to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

def findBHhalos(s,BH):
    BHhalos = BH['amiga.grp']
    return BHhalos

#
h = s.halos()  
s.physical_units()  
BHfilter = pynbody.filt.LowPass('tform',0.0) 
BH =  s.stars[BHfilter]  
BHhalos = findBHhalos(s, BH)

print(type(BHhalos)
"""" for center distance, find out what halos as in h1, h2, h3, etc... have the blackholes in them,
then make the center of the snapshot the center of each galaxy, then calculate the distance from the center
"for i in BHhalos..."  then use that sqrt i^2 j^2 k^2 from marcus' code for distance""" 

