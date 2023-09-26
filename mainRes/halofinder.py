import pynbody
import numpy as np 
import matplotlib.pyplot as plt 
from pynbody import filt, array
import pandas as pd 
import pylab 

filenamelist =  '/mnt/data0/jillian/h568/h568.cosmo75.4096gsHsbBH.000240'

nfilenames = len(filenamelist)

s = pynbody.load(filenamelist)

#initializes the command to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

def findBHhalos(s,BH):
    BHhalos = BH['amiga group']
    return BHhalos

#defines parts of the BHhalo finder
h = s.halos()
s.physical_units()
BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
BH =  s.stars[BHfilter]
BHhalos = findBHhalos(s, BH)

# not quite sure how to run these commands in the format they're in, these are placeholders
findBH(s)

findBHhalos(s,BH) 

pynbody.plot.image() 
